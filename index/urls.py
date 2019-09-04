from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.list, name="list"),
    path('searchAll', views.searchAll, name="searchAll"),
    path('details/<id>', views.details, name="details"),
    path('editPage/<id>', views.editPage, name="editPage"),
    path('edit_experiences/<id>', views.editexperiences, name="editexperiences"),
    path('edit_cases/<id>', views.editcases, name="editcases"),
    path('edit_services/<service_id>', views.editservices, name="editservices"),
    path('addservice/<id>', views.addservice, name="addservice"),
    path('accounts/profile/', views.index, name="index"),
    path('search', views.search, name="search")
]
