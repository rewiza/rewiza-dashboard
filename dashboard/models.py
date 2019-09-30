# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    link = models.CharField(max_length=255, verbose_name=_("Link"))
    image = models.ImageField(upload_to="service_images", verbose_name=_("Service image"))

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
