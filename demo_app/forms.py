from django import forms
from parler.forms import TranslatableModelForm, TranslatedField
from django.utils.translation import ugettext_lazy as _
from demo_app.models import Category


class AddCategoryForm(TranslatableModelForm):
    class Meta:
        model = Category
        fields = ('category_name',)
