from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('', views.home,name="home"),
    path('student/<int:student_id>/', views.student,name="student"),
    path("admin/", admin.site.urls),
]
