from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import Q
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.
def list_foros(request, template='list_foros.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		object_list = Foros.objects.filter(
										Q(nombre__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(contenido__icontains = q),aprobado = True).order_by('-creacion')
	else:
		object_list = Foros.objects.filter(aprobado = True).order_by('-creacion')

	foros_destacados = Foros.objects.filter(aprobado = True).annotate(count_aportes = Count('aportes')).order_by('-count_aportes')[:3]
	
	return render(request,template,locals())

def detail_foro(request, slug, template = 'detail_foro.html'):
	if request.GET.get('buscador'):
		q = request.GET['buscador']
		object_list = Foros.objects.filter(
										Q(nombre__icontains = q) |
										Q(tematica__nombre__icontains = q) |
										Q(contenido__icontains = q),aprobado = True).order_by('creacion')
		return render(request,'list_foros.html',locals())
	else:
		object = Foros.objects.get(slug = slug)
		foros_destacados = Foros.objects.filter(aprobado = True).annotate(count_aportes = Count('aportes')).exclude(id = object.id).order_by('-count_aportes')[:3]

		if request.method == 'POST':
			form = AporteForm(request.POST, request.FILES)
			if form.is_valid():
				aporte = form.save(commit=False)
				aporte.foro = object
				aporte.usuario = request.user
				aporte.save()

				try:
					subject, from_email = 'Nuevo aporte al foro ' + object.nombre, 'mail@mail.com'
					text_content = render_to_string('email/aporte.txt', {'aporte': aporte,})

					html_content = render_to_string('email/aporte.txt', {'aporte': aporte,})

					list_mail = Foros.objects.values_list('usuarios_siguiendo__email',flat=True)
					users = User.objects.filter(email__in = list_mail).exclude(id = request.user.id).values_list('email',flat=True)

					msg = EmailMultiAlternatives(subject, text_content, from_email, users)
					msg.attach_alternative(html_content, "text/html")
					msg.send()
					
					return redirect('detalle-foro', slug=object.slug)
				except:
					pass

		else:
			form = AporteForm()

		return render(request,template,locals())

@login_required
def add_comentario(request,id,template = 'add_comentario.html'):
	object = Aportes.objects.get(id = id)
	if request.method == 'POST':
		form = ComentarioForm(request.POST, request.FILES)
		if form.is_valid(): 
			comentario = form.save(commit=False)
			comentario.usuario = request.user
			comentario.aporte = object
			comentario.save()

			try:
				subject, from_email = 'Nuevo comentario al foro ' + object.foro.nombre, 'mail@mail.com'
				text_content = render_to_string('email/comentario.txt', {'obj': comentario,})

				html_content = render_to_string('email/comentario.txt', {'obj': comentario,})

				list_mail = Foros.objects.values_list('usuarios_siguiendo__email',flat=True)
				users = User.objects.filter(email__in = list_mail).exclude(id = request.user.id).values_list('email',flat=True)

				msg = EmailMultiAlternatives(subject, text_content, from_email, users)
				msg.attach_alternative(html_content, "text/html")
				msg.send()
			except:
				pass
			# return redirect('detalle-foro', slug=object.foro.slug)
	else:
		form = ComentarioForm()
	return render(request,template,locals())

@login_required
def editar_comentario(request, id, template='editar_comentario.html'):
	object = Comentarios.objects.get(id = id)
	if request.method == 'POST':
		form = ComentarioForm(request.POST, request.FILES,instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.aporte = object.aporte
			form_uncommited.usuario = request.user
			form_uncommited.save()			
			# return redirect('detalle-foro', id=object.aporte.foro.id)
	else:
		form = ComentarioForm(instance=object)

	return render(request, template, locals())

@login_required
def editar_aporte(request, id, template='editar_aporte.html'):
	object = Aportes.objects.get(id = id)
	if request.method == 'POST':
		form = AporteForm(request.POST, request.FILES,instance=object)
		if form.is_valid():
			form_uncommited = form.save()
			form_uncommited.save()

			return redirect('detalle-foro', slug=object.foro.slug)
	else:
		form = AporteForm(instance=object)

	return render(request, template, locals())

@login_required
def eliminar_aporte(request, id):
	aporte = Aportes.objects.get(id = id)
	slug_foro = aporte.foro.slug
	aporte.delete()
	return redirect('detalle-foro', slug=slug_foro)

@login_required
def eliminar_comentario(request, id):
	comment = Comentarios.objects.get(id = id)
	slug_foro = comment.aporte.foro.slug
	comment.delete()
	return redirect('detalle-foro', slug=slug_foro)

@login_required
def seguir_foro(request, id):
	foro = Foros.objects.get(id = id)
	foro.usuarios_siguiendo.add(request.user.id)
	return redirect('detalle-foro', slug=foro.slug)

@login_required
def dejar_seguir_foro(request, id):
	foro = Foros.objects.get(id = id)
	foro.usuarios_siguiendo.remove(request.user.id)
	return redirect('detalle-foro', slug=foro.slug)