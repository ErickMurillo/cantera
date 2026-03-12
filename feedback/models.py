from django.db import models

# Create your models here.
class TematicasFeedback(models.Model):
	feedback = models.TextField()

	class Meta:
		verbose_name_plural = 'Tematicas'

	def __str__(self):
		return self.feedback
