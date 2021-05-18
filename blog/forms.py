from .models import News_Post
from django import forms


class News_Post_Form(forms.ModelForm):
	"""
	Form responsible for creating new posts.
	"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	class Meta:
		"""
		Form for CRUD Operations on News_Post model.
		"""
		model = News_Post
		fields = [
			'title',
			'content',
			'categories',
			'featured',
			'post_img',
		]



