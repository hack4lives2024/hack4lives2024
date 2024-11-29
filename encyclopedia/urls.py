from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.article, name="article"),
    path("<str:q>/", views.wiki_search, name = "wiki_search"),
    path('search/', views.search, name='search')
]
