from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class UserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = User
	list_display = ['email', 'username',]
	list_display_links = ('email','username')
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'avatar', 'organizacion')}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									   'groups', 'user_permissions')}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)
 

admin.site.register(User, UserAdmin)