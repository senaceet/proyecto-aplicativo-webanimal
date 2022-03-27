import uuid

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Pets(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    history = models.TextField()
    state = models.CharField(max_length=50)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='pets', null=False, blank=False)
    image2 = models.ImageField(upload_to='pets', null=False, blank=False)
    image3 = models.ImageField(upload_to='pets', null=False, blank=False)
    image4 = models.ImageField(upload_to='pets', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Pets, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

def set_slug(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        slug= slugify(instance.name)

        while Pets.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.name, str(uuid.uuid4())[:8])
            )

        instance.slug = slug

pre_save.connect(set_slug, sender=Pets)

