from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	# below statement tells django which model should be used to create above defined form
	class Meta:
		model = Post
		fields = ('title', 'text')

class BlogEditForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text')
		