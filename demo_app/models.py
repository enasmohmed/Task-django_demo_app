from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.


class Category(TranslatableModel):
    translations = TranslatedFields(
        category_name=models.CharField(_("Category"), max_length=200, blank=False, null=False)
    )
    is_active = models.BooleanField(_("Is Active"), default=True)
    is_delete = models.BooleanField(_("Is Deleted"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)  # auto_now_add will set time when
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)  # whereas auto_now will set time when someone

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'category'
        ordering = ['-id']

    def __str__(self):
        return self.category_name
