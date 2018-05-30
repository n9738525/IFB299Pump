from django import forms
from django.contrib.auth.models import User
from book_lesson.models import Lesson, Student, Parent, Teacher, Feedback

class LessonForm(forms.ModelForm):
	Teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
	Student = Student.objects.all()
	INSTRUMENTS = (('1', 'Guitar'),('2', 'Percussion'))
	instrument = forms.ChoiceField(choices=INSTRUMENTS)
	Date = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
	Language = Student = forms.CharField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = Lesson
		fields = ('Teacher', 'Student', 'instrument', 'Date')
		
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('email', 'FirstName', 'LastName', 'DOB', 'Gender', 'phonenumber', 'facebookID')
		
class ParentProfileForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ('email', 'FirstName', 'LastName', 'DOB', 'Gender', 'phonenumber', 'parentof')
		
class FeedbackForm(forms.ModelForm):
	feedback_content = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Feedback
		fields = ('feedback_content',)