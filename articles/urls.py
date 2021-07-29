from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
	path('test/', views.test),
    path('', views.article_list.as_view(), name='list'),
    path('create/', views.article_create.as_view(), name='create'),
    path('<int:id>/', views.article_detail.as_view(), name="detail"),
    #path('<id>/edit/', views.article_edit, name="edit"),
    path('<int:id>/update/', views.article_update, name="update"),
    path('<int:id>/delete/', views.article_delete, name="delete"),
]