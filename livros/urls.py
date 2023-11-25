from django.urls import path

from . import views

app_name = 'livros'
urlpatterns = [
     path('', views.list_livros, name='index'),
     path('create/', views.create_livro, name='create'),
     path('<int:livro_id>/', views.detail_livro, name='detail'),
     path('update/<int:livro_id>/', views.update_livro, name='update'),
     path('delete/<int:livro_id>/', views.delete_livro, name='delete'),
     path('<int:livro_id>/review/', views.create_review, name='review'),
     path('lists/', views.ListListView.as_view(), name='lists'),
     path('lists/create', views.ListCreateView.as_view(), name='create-list'),
]