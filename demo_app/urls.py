from django.urls import path
from .views import CategoryList, AddCategory

app_name = 'demo_app'
urlpatterns = [
    path('category_list/', CategoryList.as_view(), name='category_list'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
]