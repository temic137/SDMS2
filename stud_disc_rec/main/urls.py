from django.urls import path

from . import views
from .views import student_login,admin_check

urlpatterns = [
    path('student/<int:pk>/',views.student,name='student'),
    path('', views.home, name='home'),
    path('staff/',views.staff,name='staff'),
    path('search_student/',views.search_student,name='search-student'),
    path('student/login/', student_login, name='student_login'),
    path('staff/login/', admin_check, name='staff_login'),
]