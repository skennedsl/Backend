from django.db import models
from django.core.exceptions import ValidationError
from geoposition.fields import GeopositionField



def validate_file_extension(value):
	import os
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.wav','.mp4','.m4a']
	if not ext in valid_extensions:
		raise ValidationError(u'File not supported!')


class Category(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.CharField(max_length=255)

	# How its displayed when printed
	def __unicode__(self):
		return '%s' % self.name


class Type(models.Model):
	name = models.CharField(max_length=255, unique=True)

	# How its displayed when printed
	def __unicode__(self):
		return '%s' % self.name
    		

class Asset(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	category = models.ForeignKey(Category)
	asset_type = models.ForeignKey(Type)

	# How its displayed when printed
	def __unicode__(self):
		return '%s' % self.name


class Location(models.Model):
	position = GeopositionField()
	asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

	# How its displayed when printed
	def __unicode__(self):
		return '%s' % self.position


class Media(models.Model):
	image = models.ImageField(upload_to='image_uploads/', null=True, blank=True)
	asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
	voice_memo = models.FileField(upload_to='voice_uploads/', help_text="Valid Extensions: .wav, .mp4, .m4a", validators=[validate_file_extension], null=True, blank=True)

	def thumbnail(self):
		return '<img width="200" src="%s"/>' % self.image.url

		