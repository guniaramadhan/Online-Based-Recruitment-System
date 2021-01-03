from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as us
from .models import Educ,User,Applicant,Application,Post_vacancy
from django import forms
from .choices import choice,gender,EDUCATION_CHOICES,kcseG
from datetime import datetime
from bootstrap_datepicker_plus import DatePickerInput
from .widgets import BootstrapDateTimePickerInput


class EducRegForm(UserCreationForm):
	typeIn = forms.ChoiceField(label='Type of Institution',choices=choice)
	name = forms.CharField(label='Name of Institution')
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
		help_texts = {'username': 'Same as your Business Registration Number.',}

class ApplicantReg(UserCreationForm):
	
	#n_id=forms.CharField(label='National ID',max_length=10,widget=forms.TextInput(attrs={'placeholder':'National ID'}) )
	#dob = forms.DateField(label='Date of Birth',widget=forms.widgets.DateInput(attrs={'type':'date'}))
	gender = forms.ChoiceField(label='Gender',choices=gender)
	#mobile=forms.CharField(label='Mobile',max_length=13,widget=forms.TextInput(attrs={'placeholder':'Phone Number'}))
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email', 'password1', 'password2']
		#help_texts = {'username': 'same as your Business Registration Number.',}



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username/Business Reg No'}))
    password = forms.CharField(widget=forms.PasswordInput)

class AddStudent(forms.Form):
	N_id=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'National ID'}))
	reg_id=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Registration No'}))
	f_name=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	l_name=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	course=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Course Done'}))
	award=forms.ChoiceField(label='',choices=EDUCATION_CHOICES)
	
	kcse=forms.ChoiceField(label='',choices=kcseG)
	dateG=forms.CharField(label='',max_length=4,widget=forms.widgets.TextInput(attrs={'placeholder':'Year Graduated'}))


class EducEditForm(forms.ModelForm):
	class Meta:
		model =User
		fields = ['email']
class Educ_EditForm(forms.ModelForm):
	class Meta:
		model = Educ
		fields = ('typeIn', 'name')


class ApplicantEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')
class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Applicant
		fields = ( 'mobile','image','cv')


class Vacancy(forms.ModelForm):
	class Meta:
		model =Application
		fields = ['duration','tsc_no']
		labels={'vacancy':'Subject Applying'}


class Personal(forms.ModelForm):
	class Meta:
		model =Application
		fields = ['surname','m_name','l_name','id_no','image_id']


class Academic(forms.ModelForm):
	class Meta:
		model =Application
		fields = ['institutionA','award','kcse','image_cert','image_certKC','break_in']
		labels={'institutionA':'Institution Attended'}

class Other(forms.ModelForm):
	class Meta:
		model =Application
		fields = ['co_curriculum','image_co','leadership','image_lead']


class DatePicker(DatePickerInput):
	template_name='bootstrap_datetimepicker.html'



class post_vacancy(forms.ModelForm):
	
	class Meta:
		model =Post_vacancy
		fields = ['subjects','advert','descrip','num_req','start','end']
		widgets={'start':forms.DateInput(attrs={'class':'datepicker','id':'start'}),
				'end':forms.DateInput(attrs={'class':'datepicker','id':'end'})}
		