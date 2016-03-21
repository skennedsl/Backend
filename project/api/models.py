from django.db import models
from django.core.exceptions import ValidationError
from geoposition.fields import GeopositionField
import os
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

def validate_file_extension(value):
	import os
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.aac','.wav','.mp4','.m4a']
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
	description = models.CharField(max_length=255, blank=True)
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


class MediaImage(models.Model):
	image = models.ImageField(upload_to='image_uploads/', null=True, blank=True)
	asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

	def thumbnail(self):
		return '<img width="200" src="%s"/>' % self.image.url

	def save(self, *args, **kwargs):
		# delete old file when replacing by updating the file
		try:
			this = MediaImage.objects.get(id=self.id)
			if this.image != self.image:
				this.image.delete(save=False)
		except:
			pass  # when new photo then we do nothing, normal case
		super(MediaImage, self).save(*args, **kwargs)

class MediaVoiceMemo(models.Model):
	asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
	voice_memo = models.FileField(upload_to='voice_uploads/', help_text="Valid Extensions: .aac, .wav, .mp4, .m4a", validators=[validate_file_extension], null=True, blank=True)

	def save(self, *args, **kwargs):
		# delete old file when replacing by updating the file
		try:
			this = MediaVoiceMemo.objects.get(id=self.id)
			if this.voice_memo != self.voice_memo:
				this.voice_memo.delete(save=False)
		except:
			pass  # when new photo then we do nothing, normal case
		super(MediaVoiceMemo, self).save(*args, **kwargs)


@receiver(pre_delete, sender=MediaImage)
def media_image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)

@receiver(pre_delete, sender=MediaVoiceMemo)
def media_voice_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.voice_memo.delete(False)

		