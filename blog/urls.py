from django.urls import path

from blog import views

#   page/
#   article/
#   category/
#   tag/

urlpatterns = [
    path(r'', views.article_year, name='index'),

    # path(r'page/')
]
