from django import forms


class UserForm(forms.Form):
	name = forms.CharField(label="Название задачи", help_text="Введите название задачи")
	desc = forms.CharField(label="Описание", widget=forms.Textarea)
	# age = forms.IntegerField(label="Возраст")
