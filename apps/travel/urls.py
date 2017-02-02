from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$", views.index, name = "main"),
    url(r"^new$", views.new, name = "new_trip"),
    url(r"^add$", views.add, name = "add_trip"),
    url(r"^join/(?P<trip_id>\d+)$", views.join, name = "join_trip"),
    url(r"^show/(?P<trip_id>\d+)$", views.show, name = "show_trip")
]
