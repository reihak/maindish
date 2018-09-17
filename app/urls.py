from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_id>', views.detail, name='detail'),
    path('new_menu', views.new_menu, name='new_menu'),
    path('delete_menu/<int:menu_id>', views.delete_menu, name='delete_menu'),
    path('edit_menu/<int:menu_id>', views.edit_menu, name='edit_menu'),
    path('weekly', views.weekly, name='weekly'),
]
