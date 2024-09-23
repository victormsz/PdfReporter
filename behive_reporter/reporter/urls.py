from django.urls import path


from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("templates/", views.templates, name="templates"),
    path("templates/<int:idtemplate>/", views.templates_id, name="templates_id"),
]