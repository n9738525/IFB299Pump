
from django.shortcuts import render
from django.http import HttpResponse
from book_lesson.forms import LessonForm, UserForm, StudentProfileForm
from django.template import loader

from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_lesson(request):
	if request.method == 'POST':
		form = LessonForm(request.POST)
		
		if form.is_valid():
            # Save the new category to the database.
			form.save(commit=True)
			
			return index(request)
			
		else:
            # The supplied form contained errors - just print them to the terminal.
			print(form.errors)
			
	else:
        # If the request was not a POST, display the form to enter details.
		form = LessonForm()
	
	template = loader.get_template('book_lesson/add_lesson.html')	
		
	return HttpResponse(template.render({'form': form}, request))
	
	
def register(request):
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		student_profile_form = StudentProfileForm(data=request.POST)
		
		if user_form.is_valid() and student_profile_form.is_valid():
			user = user_form.save()
			
			user.set_password(user.password)
			user.save()
			
			profile = student_profile_form.save(commit=False)
			profile.username = user
			
			
			profile.save()
			
			registered = True
			
		else:
			print(user_form.errors, student_profile_form.errors)
			
	else:
		user_form = UserForm()
		student_profile_form = StudentProfileForm()
			
	template = loader.get_template('book_lesson/register.html')
	
	return HttpResponse(template.render({'user_form': user_form, 'student_profile_form': student_profile_form, 'registered': registered}, request))		
			
