from django.contrib import admin
from .models import Gender, Grade, GuardianRelation,Student, Designation, Subject, EmploymentStatus, Staff, ClassAndTiming, Staff, ClassIncharge, FAQs, StudentApplication, Timing
# Register your models here.

'''
///////////////////////
//   Student     //
///////////////////////
'''
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class GuardianRelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'grade', 'age', 'gender', 'dob','guardian_name', 'guardian_relation', 'address', 'date_of_enrollment', 'email', 'phone','emergency_phone' , 'previous_school', 'status')


class StudentApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username' ,'grade', 'age', 'gender', 'dob','guardian_name', 'guardian_relation', 'address', 'email', 'phone','emergency_phone' , 'previous_school', 'is_registered', 'seen')


admin.site.register(Gender, GenderAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(GuardianRelation, GuardianRelationAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentApplication, StudentApplicationAdmin)
'''
///////////////////////
//   Staff     //
///////////////////////
'''

class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class EmployStatusAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','dob', 'gender', 'qualification', 'experience', 'designation', 'subject', 'email', 'phone', 'emergency_phone', 'address', 'joining_date', 'salary', 'employment_status', 'contract_details', 'status')

admin.site.register(Designation, DesignationAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(EmploymentStatus, EmployStatusAdmin)
admin.site.register(Staff, StaffAdmin)


'''
//////////////////
//   Timing     //
//////////////////
'''

class TimingAdmin(admin.ModelAdmin):
    list_display = ('id', 'period_name', 'period_from', 'period_to')

admin.site.register(Timing, TimingAdmin)



'''
///////////////////////////
//   ClassAndTime     //
///////////////////////////
'''

class ClassAndTimingAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'period_one', 'period_one_subject', 'period_one_teacher', 'period_two', 'period_two_subject', 'period_two_subject', 'period_three', 'period_three_subject', 'period_three_teacher', 'period_four', 'period_four_subject', 'period_four_teacher', 'period_five', 'period_five_subject', 'period_five_teacher', 'period_six', 'period_six_subject', 'period_six_teacher', 'period_seven', 'period_seven_subject', 'period_seven_teacher', 'status')


class ClassInchargeAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'class_obj')

admin.site.register(ClassAndTiming, ClassAndTimingAdmin)
admin.site.register(ClassIncharge, ClassInchargeAdmin)


'''
///////////////////////////
//   FAQs     //
///////////////////////////
'''

class FAQsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'status')


admin.site.register(FAQs, FAQsAdmin)

