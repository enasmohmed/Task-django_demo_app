from django.shortcuts import render
from django.views.generic import ListView, CreateView
from parler.views import TranslatableCreateView

from demo_project.settings import PARLER_LANGUAGES
from .forms import AddCategoryForm
from .models import Category


# Create your views here.

class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category_data'
    paginate_by = 10
    queryset = Category.objects.all()


class AddCategory(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'add_category.html'
    success_url = "/category/category_list/"


