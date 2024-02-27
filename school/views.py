from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

# models
from .models import Student, Staff, Grade, Gender, Role, Subject, EmploymentStatus, ClassAndTiming, GuardianRelation, ClassIncharge
from django.contrib.auth.models import User


# forms
from django.contrib.auth.forms import UserCreationForm
from .forms.user_creation_form import SignupForm
from .forms.add_student_form import AddStudentForm
from .forms.add_staff_form import AddStaffForm
from .forms.add_grade_form import AddGradeForm
from .forms.add_class_and_timing import AddClassAndTimingForm
from .forms.add_gender_form import AddGenderForm
from .forms.add_class_incharge import AddClassInchargeForm
from .forms.add_guardian_relation_form import AddGuardianRelationForm
from .forms.add_role import AddRoleForm
from .forms.add_subject_form import AddSubjectForm



from django.contrib.auth import login, logout, authenticate 

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
    return render(request, 'contact.html')

def locations(request):
    return render(request, 'locations.html')

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! You\'ve successfully signed up!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid entries! Please try again.')
            return redirect('signup')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        if not request.user.is_authenticated:
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                user = authenticate(request, username=username, password=password)
                if user is None:
                    messages.error(request, 'User not found!')
                    return redirect('login')
                else:
                    login(request, user)
                    messages.success(request, 'User logged in successfully!')
                    return redirect('home')
            else:
                messages.error(request, 'Please enter both username and password!')
                return redirect('login')
        else:
            messages.warning(request, 'You have already logged in!')
            return redirect('home')

def user_logout(request):
    if request.user.is_authenticated:
        messages.success(request,'Logged out successfully!')
        logout(request)
    else:
        messages.error(request, 'You already have logged out!')
    return redirect('home')

'''
///////////////////////////////////////////////////////////////////////////////
                                //   Admin     //
///////////////////////////////////////////////////////////////////////////////
''' 

def portal(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            total_students = Student.objects.count()
            total_staff = Staff.objects.count()
            return render(request, 'portal.html', {'total_students': total_students, 'total_staff': total_staff})
        else:
            messages.warning(request, 'This page is for admins only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')
'''
///////////////////////
//   Students     //
///////////////////////
''' 

def display_students(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            data = Student.objects.all()
            return render(request, 'display_students.html', {'data': data})
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')    
        
def student_details(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            student = Student.objects.get(pk=id)
            return render(request, 'student_details.html', {'student': student})
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')
    
def add_student(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'GET':
                form = AddStudentForm()
                return render(request, 'add_student.html', {'form': form})
            else:
                form = AddStudentForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,'The student has been added successfully!')
                    return redirect('display_students')
                else:
                    messages.error(request, 'Please enter the valid Information!')
                    return redirect('add_student')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def edit_student(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_student = Student.objects.get(pk=id)
            if request.method == 'GET':
                form = AddStudentForm(instance=current_student)
                return render(request, 'edit_student.html',{'form': form, 'id':id})
            else:
                form = AddStudentForm(request.POST, instance=current_student)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Student updated successfully!')
                    return redirect('display_students')
                else:
                    messages.error(request, 'please enter valid information!')
                    return redirect('edit_student', id=id)
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def change_student_status(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_student = get_object_or_404(Student, pk=id)
            current_student.status = not current_student.status
            current_student.save()
            messages.success(request, f'Student {id} status updated successfully')
            return redirect('display_students')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def delete_student(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_student = Student.objects.get(pk=id)
            current_student.delete()
            messages.success(request, f'The student {id} has been deleted successfully!')
            return redirect('display_students')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

'''
///////////////////////
//   staff     //
///////////////////////
'''

def display_staff(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            staff = Staff.objects.all() 
            return render(request, 'display_staff.html', {'staff': staff})
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def staff_details(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            staff = get_object_or_404(Staff, pk=id)
            return render(request, 'staff_details.html', {'staff': staff})
        else:
                messages.warning(request, 'This page is for admin only!')
                return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')
    
def change_staff_status(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_employ = get_object_or_404(Staff, pk=id)
            current_employ.status = not current_employ.status
            current_employ.save()
            messages.success(request, f'Employ {id} status updated Successfully!')
            return redirect('display_staff')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def add_staff(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'GET':
                form = AddStaffForm()
                return render(request, 'add_staff.html', {'form': form})
            else:
                form = AddStaffForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'New staff added successfully!')
                    return redirect('display_staff')
                else:
                    messages.error(request, 'Please enter valid information!')
                    return redirect('add_staff')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def edit_staff(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_employ = get_object_or_404(Staff, pk=id)
            if request.method == 'GET':
                form = AddStaffForm(instance=current_employ)
                return render(request, 'edit_staff.html', {'form':form, 'id':id})
            else:
                form = AddStaffForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, f'Employ {id} has been updated successfully!')
                    return redirect('display_staff')
                else:
                    messages.error(request, 'Please enter the valid information!')
                    return redirect('edit_staff', id=id)
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def delete_staff(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_employ = get_object_or_404(Staff, pk=id)
            current_employ.delete()
            messages.success(request, f'Employ {id} deleted successfully')
            return redirect('display_staff')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

'''
//////////////////////////////////////
//   classes and timing     //
//////////////////////////////////////
''' 

def display_classes(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            data = ClassAndTiming.objects.all()
            return render(request, 'display_classes.html', { 'data' : data })
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def change_class_status(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_class = ClassAndTiming.objects.get(pk=id)
            current_class.status = not current_class.status
            current_class.save()
            messages.success(request, f'Class {current_class.class_name} status changed successfully!')
            return redirect('display_classes')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')
    
def class_details(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            data = ClassAndTiming.objects.get(id=id)
            return render(request, 'class_details.html', { 'class':data })
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def add_class(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            a_class = ClassAndTiming.objects.all().first()
            if request.method=='GET':
                form = AddClassAndTimingForm(instance=a_class)
                return render(request, 'add_class.html', { 'form' : form })
            else:
                # .first() method is used to get the first object and if there is no object it will return None.
                check_existence = ClassAndTiming.objects.filter(class_name=request.POST['class_name']).first()
                if check_existence is None:
                    form = AddClassAndTimingForm(request.POST)
                    if form.is_valid():
                        form.save()
                        messages.success(request, 'New class added successfully')
                        return redirect('display_classes')
                    else:
                        messages.error(request, 'Invalid entries please try again')
                        return redirect('add_class')
                else:
                    messages.error(request, 'Class already exists please chose another class!')
                    return redirect('add_class')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def edit_class(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_class = get_object_or_404(ClassAndTiming, id=id)
            if request.method == 'GET':
                form = AddClassAndTimingForm(instance=current_class)
                return render(request, 'edit_class.html', {'form': form, 'id':id})
            else:
                form = AddClassAndTimingForm(request.POST, instance=current_class)
                if form.is_valid():
                    form.save()
                    messages.success(request, f'Class {id} has been updated successfully!')
                    return redirect('display_classes')
                else:
                    messages.error(request, form.errors)
                    return redirect('edit_class', id=id)
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def delete_class(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_class = get_object_or_404(ClassAndTiming, id=id)
            current_class.delete()
            messages.success(request, f'Grade {id} has been deleted successfully!')
            return redirect('display_classes')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

'''
////////////////////////////////////////
//   Class Incharges     //
////////////////////////////////////////
''' 

def display_class_incharges(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            data = ClassIncharge.objects.all()
            return render(request, 'display_class_incharges.html',{'data':data})
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def add_class_incharge(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'GET':
                form = AddClassInchargeForm()
                return render(request, 'add_class_incharge.html', {'form':form})
            else:
                form = AddClassInchargeForm(request.POST)
                if form.is_valid():
                    check_existence_teacher = ClassIncharge.objects.filter(teacher=request.POST['teacher']).first()
                    check_existence_class = ClassIncharge.objects.filter(class_obj=request.POST['class_obj']).first()
                    if check_existence_teacher:
                        messages.error(request, 'The selected teacher is already holding a class.chose anothor teacher!')            
                        return redirect('add_class_incharge')
                    elif check_existence_class:
                        messages.error(request, 'An incharge is already assigned to this class please choose a different Class.')
                        return redirect('add_class_incharge')
                    else:
                        form.save()
                        messages.success(request, 'New class incharge added successfully')
                        return redirect('display_class_incharges')
                else:
                    messages.error(request, 'Invalid entries! Please enter the valid entries.')
                    return redirect('add_class_incharge')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def edit_class_incharge(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_class_incharge = ClassIncharge.objects.get(pk=id)
            if request.method == 'GET':
                form = AddClassInchargeForm(instance=current_class_incharge)
                return render(request, 'edit_class_incharge.html', {'form': form, 'id':id})
            else:
                form = AddClassInchargeForm(request.POST, instance=current_class_incharge)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Class Incharge was successfully updated.')
                    return redirect('display_class_incharges')
                else:
                    messages.error(request, 'Invalid entries! please enter the valid entries.')
                    return redirect('edit_class_incharge', id=id)
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def delete_class_incharge(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_class_incharge = ClassIncharge(pk=id)
            current_class_incharge.delete()
            messages.success(request, 'The class was successfully deleted.')
            return redirect('display_class_incharges')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

'''
///////////////////////
//   grades     //
///////////////////////
''' 

def display_grades(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            data = Grade.objects.all()
            return render(request, 'display_grades.html', {'data': data})
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def add_grade(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'GET':
                form = AddGradeForm()
                return render(request, 'add_grade.html', {'form': form})
            else:
                form = AddGradeForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'New Grade added successfully!')
                    return redirect('display_grades')
                else:
                    messages.error(request, 'Invalid entries please try again!')
                    return redirect('add_grade')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def edit_grade(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_grade = Grade.objects.get(pk=id)
            if request.method == 'GET':
                form = AddGradeForm(instance=current_grade)
                return render(request, 'edit_grade.html', {'form':form,'id':id})
            else:
                form = AddGradeForm(request.POST,instance=current_grade)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Added new grade successfully!')
                    return redirect('display_grades')
                else:
                    messages.error(request, 'Invalid entry please try again!')
                    return redirect('edit_grades', id=id)
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')
        
def delete_grade(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:        
            current_grade = Grade.objects.get(id=id)
            current_grade.delete()
            messages.success(request, f'Grade {id} has been deleted successfully!')
            return redirect('display_grades')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')


'''
///////////////////////
//   Genders    //
///////////////////////
''' 

def display_genders(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            data = Gender.objects.all()
            return render(request, 'display_genders.html', {'data': data})
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def add_gender(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'GET':
                form = AddGenderForm()
                return render(request, 'add_gender.html', {'form': form})
            else:
                form = AddGenderForm(request.POST)
                check_exists = Gender.objects.filter(name=request.POST['name']).first()
                if check_exists:
                    messages.error(request, 'Gender already exists')
                    return redirect('add_gender')
                else:
                    if form.is_valid():
                        form.save()
                        messages.success(request, 'New Gender added successfully!')
                        return redirect('display_genders')
                    else:
                        messages.error(request, 'Invalid entries please try again!')
                        return redirect('add_gender')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def edit_gender(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_gender = Gender.objects.get(pk=id)
            if request.method == 'GET':
                form = AddGenderForm(instance=current_gender)
                return render(request, 'edit_gender.html', {'form':form,'id':id})
            else:
                form = AddGenderForm(request.POST,instance=current_gender)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Added new gender successfully!')
                    return redirect('display_genders')
                else:
                    messages.error(request, 'Invalid entry please try again!')
                    return redirect('edit_gender', id=id)
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def delete_gender(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_gender = Gender.objects.get(id=id)
            current_gender.delete()
            messages.success(request, f'Gender {id} has been deleted successfully!')
            return redirect('display_genders')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')
'''
//////////////////////////////////////
//   Guardian Relation     //
//////////////////////////////////////
''' 

def display_guardian_relations(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            data = GuardianRelation.objects.all()
            return render(request, 'display_guardian_relations.html', {'data': data})
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def add_guardian_relation(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'GET':
                form = AddGuardianRelationForm()
                return render(request, 'add_guardian_relation.html', {'form': form})
            else:
                form = AddGuardianRelationForm(request.POST)
                check_existence = GuardianRelation.objects.filter(name=request.POST['name']).first()
                if check_existence:
                    messages.error(request, 'Guardian relation you entered already exists')
                    return redirect('add_guardian_relation')
                else:
                    if form.is_valid():
                        form.save()
                        messages.success(request, 'New Guardian relation added successfully')
                        return redirect('display_guardian_relations')
                    else:
                        messages.error(request, 'Invalid entry! Please enter the valid entry.')
                        return redirect('add_guardian_relation')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def edit_guardian_relation(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_guardian_relation = GuardianRelation.objects.get(pk=id)
            if request.method == 'GET':
                form = AddGuardianRelationForm(instance=current_guardian_relation)
                return render(request, 'edit_guardian_relation.html', {'form':form,'id':id})
            else:
                form = AddGuardianRelationForm(request.POST,instance=current_guardian_relation)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Guardian relation updated successfully!')
                    return redirect('display_guardian_relations')
                else:
                    messages.error(request, 'Invalid entry please try again!')
                    return redirect('edit_guardian_relation', id=id)
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def delete_guardian_relation(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_guardian_relation = GuardianRelation.objects.get(id=id)
            current_guardian_relation.delete()
            messages.success(request, 'Guardian relation deleted successfully!')
            return redirect('display_guardian_relations')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

'''
///////////////////////
//   Role     //
///////////////////////
''' 

def display_roles(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            data = Role.objects.all()
            return render(request, 'display_roles.html', {'data': data})
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def add_role(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'GET':
                form = AddRoleForm()
                return render(request, 'add_role.html', {'form': form})
            else:
                form = AddRoleForm(request.POST)
                check_existence = Role.objects.filter(name=request.POST['name']).first()
                if check_existence:
                    messages.error(request, 'Role you entered already exists')
                    return redirect('add_role')
                else:
                    if form.is_valid():
                        form.save()
                        messages.success(request, 'New Role added successfully')
                        return redirect('display_roles')
                    else:
                        messages.error(request, 'Invalid entry! Please enter the valid entry.')
                        return redirect('add_role')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def edit_role(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_role = Role.objects.get(pk=id)
            if request.method == 'GET':
                form = AddRoleForm(instance=current_role)
                return render(request, 'edit_role.html', {'form':form,'id':id})
            else:
                form = AddRoleForm(request.POST,instance=current_role)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Role updated successfully!')
                    return redirect('display_roles')
                else:
                    messages.error(request, 'Invalid entry please try again!')
                    return redirect('edit_role', id=id)
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def delete_role(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_role = Role.objects.get(id=id)
            current_role.delete()
            messages.success(request, 'Role deleted successfully!')
            return redirect('display_roles')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

'''
///////////////////////
//   Subjects    //
///////////////////////
''' 

def display_subjects(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            data = Subject.objects.all()
            return render(request, 'display_subjects.html', {'data':data})
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def add_subject(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'GET':
                form = AddSubjectForm()
                return render(request, 'add_subject.html', {'form': form})
            else:
                form = AddSubjectForm(request.POST)
                check_existence = Subject.objects.filter(name=request.POST['name']).first()
                if check_existence:
                    messages.error(request, 'Subject you entered already exists')
                    return redirect('add_subject')
                else:
                    if form.is_valid():
                        form.save()
                        messages.success(request, 'New Subject added successfully')
                        return redirect('display_subjects')
                    else:
                        messages.error(request, 'Invalid entry! Please enter the valid entry.')
                        return redirect('add_subject')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def edit_subject(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_subject = Subject.objects.get(pk=id)
            if request.method == 'GET':
                form = AddSubjectForm(instance=current_subject)
                return render(request, 'edit_subject.html', {'form':form,'id':id})
            else:
                form = AddSubjectForm(request.POST,instance=current_subject)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Subject updated successfully!')
                    return redirect('display_subjects')
                else:
                    messages.error(request, 'Invalid entry please try again!')
                    return redirect('edit_subject', id=id)
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

def delete_subject(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            current_subject = Subject.objects.get(id=id)
            current_subject.delete()
            messages.success(request, 'Subject deleted successfully!')
            return redirect('display_subjects')
        else:
            messages.warning(request, 'This page is for admin only!')
            return redirect('home')
    else:
        messages.warning(request, 'please login first!')
        return redirect('home')

'''
///////////////////////////////////////////////////////////////////////////////
                                //   Teacher     //
///////////////////////////////////////////////////////////////////////////////
''' 

def teacher_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            current_teacher = Staff.objects.filter(email=request.user.email).first()
            if current_teacher is None:
                messages.success(request, 'Only teachers are allowed to access this page.')
                return redirect('home')
            else:
                incharge = ClassIncharge.objects.filter(teacher=current_teacher).first()
            if incharge is None:
                messages.warning(request, 'You are not the In-charge of any class.')
                return redirect('teacher_dashboard')
            else:
                grade = Grade.objects.filter(name = incharge.class_obj.class_name).first()
                class_and_timing = ClassAndTiming.objects.filter(class_name = grade).first()
                return render(request, 'teacher_dashboard.html' ,{'teacher':current_teacher, 'class':class_and_timing})
        else:
            messages.warning(request, 'This page is for staff only.')
            return redirect('home')
    else:
        messages.warning(request, 'Please login first!')
        return redirect('login')

'''
///////////////////////////////////////////////////////////////////////////////
                                //   Student     //
///////////////////////////////////////////////////////////////////////////////
''' 

def student_dashboard(request):
    if request.user.is_authenticated:
        if not request.user.is_staff:
            current_student = Student.objects.filter(email=request.user.email).first()
            if current_student is None:
                messages.warning(request, 'This page is only for students!')
                return redirect('home')
            grade = Grade.objects.filter(name=current_student.grade).first()
            class_and_timing = ClassAndTiming.objects.filter(class_name = grade).first()
            return render(request, 'student_dashboard.html', {'current_student': current_student, 'class':class_and_timing})
        else:
            messages.warning(request, "Staff can't access this page!")
            return redirect('home')
    else:
        messages.warning(request, 'Please login first!')
        return redirect('login')