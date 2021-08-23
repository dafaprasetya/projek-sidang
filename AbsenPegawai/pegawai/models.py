from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
	nama		= models.ForeignKey(User, related_name='absenn', on_delete=models.CASCADE)
	waktu		= models.DateTimeField(auto_now_add = True)
	jenis		= [
		('Hadir', 'Hadir'),
		('Sakit', 'Sakit'),
		('Izin', 'Izin'),
		('Tanpa Keterangan', 'Tanpa Keterangan')
	]
	kategori	= models.CharField(max_length=50, choices= jenis, default="Hadir")
	slug		= models.SlugField(blank=True, editable = False)
	def get_absolute_url(self):
		return reverse("index")
	

	def save(self):

        
		self.slug = slugify(self.nama) + str(self.waktu)
		return super(Post, self).save() 

	def __str__(self):
		return "{}. {}".format(self.id,self.nama)