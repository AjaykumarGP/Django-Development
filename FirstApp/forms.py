
from django import forms
from django.core import validators
from django.forms import ModelForm
from .models import StudentInfo, UserInfo

#custom validator
def checkInputSize(value):
	if len(value) <= 5:
		raise forms.ValidationError("Input side should be greater than 5")

class BasicForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	verifyEmail = forms.EmailField()
	text = forms.CharField(widget = forms.Textarea,
							validators=[checkInputSize])

	botCatcher = forms.CharField(required = False,
								widget = forms.HiddenInput,
								validators = [validators.MaxLengthValidator(0)])


	# clean_variableName() - build-in function for botcathcer
	def clean_botCatcher(self):
		botCatcher = self.cleaned_data['botCatcher']

		if len(botCatcher) > 0:
			raise forms.ValidationError("Found the bot")
		return botCatcher

	# clean() - build-in function to clean all the frm data at once
	def clean(self):
		cleanedData = super().clean()
		email = cleanedData["email"]
		verifyEmail = cleanedData["verifyEmail"]

		if email != verifyEmail:
			raise forms.ValidationError("Email did not match")


class StudentInfoForm(ModelForm):
	class Meta:
		model = StudentInfo
		fields = "__all__"

class UserInfoForm(ModelForm):
	class Meta:
		model = UserInfo
		fields = ('firstName', 'lastName', 'email')