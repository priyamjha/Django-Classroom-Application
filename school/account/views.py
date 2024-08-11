from django.shortcuts import get_object_or_404, render, redirect
from .forms import ClassroomForm, LoginForm, TeacherSignUpForm, StudentSignUpForm, TimetableForm
from django.contrib.auth import authenticate, login, logout
from .models import Classroom, Timetable, User  # Make sure this import is correct
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def delete_teacher(request, pk):
    teacher = get_object_or_404(User, pk=pk, is_teacher=True)
    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'Teacher deleted successfully.')
        return redirect('teacher_details')
    else:
        messages.warning(request, "Invalid request method.")
        return redirect('teacher_details')


@login_required
def delete_student(request, pk):
    student = get_object_or_404(User, pk=pk, is_student=True)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('student_details')
    else:
        messages.warning(request, "Invalid request method.")
        return redirect('student_details')

@login_required
def delete_classroom(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.method == 'POST':
        classroom.delete()
        messages.success(request, 'Classroom deleted successfully.')
        return redirect('classroom_list')
    else:
        messages.warning(request, "Invalid request method.")
        return redirect('classroom_list')

@login_required
def delete_timetable(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        timetable.delete()
        messages.success(request, 'Timetable deleted successfully.')
        return redirect('timetable_list')
    else:
        messages.warning(request, "Invalid request method.")
        return redirect('timetable_list')



@login_required
def update_teacher(request, pk):
    teacher = get_object_or_404(User, pk=pk, is_teacher=True)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
        else:
            teacher.username = username
            teacher.email = email
            if password1:  # If the user entered a new password
                teacher.set_password(password1)
            teacher.save()
            messages.success(request, 'Teacher updated successfully.')
            return redirect('teacher_details')

    return render(request, 'update_teacher.html', {'teacher': teacher})


@login_required
def update_student(request, pk):
    student = get_object_or_404(User, pk=pk, is_student=True)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 and password1 != password2:
            messages.error(request, 'Passwords do not match.')
        else:
            student.username = username
            student.email = email
            if password1:
                student.set_password(password1)
            student.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('student_details')

    return render(request, 'update_student.html', {'student': student})

@login_required
def update_classroom(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        active_days = request.POST.get('active_days')

        classroom.name = name
        classroom.start_time = start_time
        classroom.end_time = end_time
        classroom.active_days = active_days
        classroom.save()
        messages.success(request, 'Classroom updated successfully.')
        return redirect('classroom_list')

    return render(request, 'update_classroom.html', {'classroom': classroom})

@login_required
def update_timetable(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        classroom = request.POST.get('classroom')
        subject = request.POST.get('subject')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        days = request.POST.get('days')

        timetable.classroom.name = classroom
        timetable.subject = subject
        timetable.start_time = start_time
        timetable.end_time = end_time
        timetable.days = days
        timetable.save()
        messages.success(request, 'Timetable updated successfully.')
        return redirect('timetable_list')

    return render(request, 'update_timetable.html', {'timetable': timetable})



@login_required
def classroom_list(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classroom_list.html', {'classrooms': classrooms})


@login_required
def timetable_list(request):
    timetables = Timetable.objects.all()
    return render(request, 'timetable_list.html', {'timetables': timetables})


@login_required
def create_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classroom created successfully.')
            return redirect('principalpage')
        else:
            for error in form.errors.values():
                messages.warning(request, error)
    else:
        form = ClassroomForm()
    
    return render(request, 'create_classroom.html', {'form': form})

@login_required
def create_timetable(request):
    classrooms = Classroom.objects.all()

    if request.method == 'POST':
        classroom_id = request.POST.get('classroom')
        subject = request.POST.get('subject')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        days = request.POST.get('days')

        classroom = Classroom.objects.get(id=classroom_id)

        # Create Timetable
        Timetable.objects.create(
            classroom=classroom,
            subject=subject,
            start_time=start_time,
            end_time=end_time,
            days=days
        )

        messages.success(request, 'Timetable created successfully.')
        # Check the user role and redirect accordingly
        if request.user.is_principal:
            return redirect('principalpage')
        elif request.user.is_teacher:
            return redirect('teacherpage')

    context = {
        'classrooms': classrooms,
    }
    
    return render(request, 'create_timetable.html', context)




@login_required
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Teacher account created successfully.')
            return redirect('principalpage') # Make sure this URL is defined in your project
        else:
            messages.warning(request, 'Error validating form')
    else:
        form = TeacherSignUpForm()
    return render(request, 'register_teacher.html', {'form': form})


@login_required
def student_register(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Student account created successfully.')
            if request.user.is_principal:
                return redirect('principalpage')
            elif request.user.is_teacher:
                return redirect('teacherpage')
        else:
            messages.warning(request, 'Error validating form')
    else:
        form = StudentSignUpForm()
    return render(request, 'register_student.html', {'form': form})



def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None
            
            if user and user.check_password(password):
                login(request, user)
                if user.is_principal:
                    return redirect('principalpage')
                elif user.is_teacher:
                    return redirect('teacherpage')
                elif user.is_student:
                    return redirect('studentpage')
            else:
                messages.warning(request, 'Invalid credentials')
        else:
            messages.warning(request, 'Error validating form')
    return render(request, 'login.html', {'form': form})



def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has been ended. Please log in to continue')
    return redirect('login_view')



def principal(request):
    return render(request, 'principal.html')

def teacher(request):
    return render(request, 'teacher.html')

def student(request):
    return render(request, 'student.html')


@login_required
def teacher_details(request):
    teachers = User.objects.filter(is_teacher=True)
    return render(request, 'teacher_details.html', {'teachers': teachers})

@login_required
def student_details(request):
    students = User.objects.filter(is_student=True)
    return render(request, 'student_details.html', {'students': students})