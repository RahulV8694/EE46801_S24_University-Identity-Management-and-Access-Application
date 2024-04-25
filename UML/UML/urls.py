from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Clarkson Admin Dashboard"
admin.site.site_title = "Clarkson Admin"
admin.site.index_title = "Clarkson Administration"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myProject.urls")),
]
