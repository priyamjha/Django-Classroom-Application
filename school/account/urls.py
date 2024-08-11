from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_user, name='logout'),
    
    path('principalpage/', views.principal, name='principalpage'),
    
    path('teacher/', views.teacher, name='teacherpage'),
    
    path('student/', views.student, name='studentpage'),
    
    path('register/teacher/', views.teacher_register, name='teacher_register'),
    path('register/student/', views.student_register, name='student_register'),
    
    path('teachers/', views.teacher_details, name='teacher_details'),
    path('students/', views.student_details, name='student_details'),
    
    path('create_classroom/', views.create_classroom, name='create_classroom'),
    path('create_timetable/', views.create_timetable, name='create_timetable'),
    
    path('classrooms/', views.classroom_list, name='classroom_list'),
    path('timetables/', views.timetable_list, name='timetable_list'),
    
    path('update-teacher/<int:pk>/', views.update_teacher, name='update_teacher'),
    path('delete-teacher/<int:pk>/', views.delete_teacher, name='delete_teacher'),
    path('update-student/<int:pk>/', views.update_student, name='update_student'),
    path('delete-student/<int:pk>/', views.delete_student, name='delete_student'),
    path('update-classroom/<int:pk>/', views.update_classroom, name='update_classroom'),
    path('delete-classroom/<int:pk>/', views.delete_classroom, name='delete_classroom'),
    path('update-timetable/<int:pk>/', views.update_timetable, name='update_timetable'),
    path('delete-timetable/<int:pk>/', views.delete_timetable, name='delete_timetable'),
]
