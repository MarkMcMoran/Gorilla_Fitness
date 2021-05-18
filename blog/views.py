from django.shortcuts import  redirect
from django.urls import reverse_lazy
from .models import News_Post
from .forms import News_Post_Form
from django.views.generic import (
	CreateView,
	ListView,
	UpdateView,
	DetailView,
	DeleteView
)

"""

These classes do CRUD Operations by using the News_Post 
PostCreateView()
PostDeleteView()
PostUpdateView()
NewsListView()
PostDetailView()

"""


class PostUpdateView(UpdateView):
	""" View responsible for modification of pre-existing views """
	model = News_Post
	template_name = 'blog/create_post.html'
	form_class = News_Post_Form
	queryset = News_Post.objects.all()

	def get_context_data(self, **kwargs):
		""" Pulls the necessary context data, and sets the title as 'Update' """
		context = super().get_context_data(**kwargs)
		context['title'] = 'Update'
		return context

	def form_valid(self, form):
		""" Logic for ensuring form information is valid. """
		form.save()
		return redirect(reverse_lazy('post_detail', kwargs={
			'pk': form.instance.pk
		}))


class PostCreateView(CreateView):
	""" View for creating posts. """
	model = News_Post
	template_name = 'blog/create_post.html'
	form_class = News_Post_Form

	def get_context_data(self, **kwargs):
		""" Pulls the necessary context data, and sets the title as 'Create' """
		context = super().get_context_data(**kwargs)
		context['title'] = 'Create'
		return context

	def form_valid(self, form):
		""" Redirects to postdetail/<pk> if form submission was valid. """
		form.save()
		return redirect(reverse_lazy("post_detail", kwargs={
			'pk': form.instance.pk
		}))




class NewsListView(ListView):
	""" Paginated view for blog posts created. """
	template_name = 'news_post_list.html'
	model = News_Post
	queryset = News_Post.objects.filter(featured=True)
	paginate_by = 2
	ordering = ['-date_posted']
	most_recent = News_Post.objects.order_by('-date_posted')[:3]

	def get_context_data(self, **kwargs):
		""" Specifies queryset, passes through page numbers for paginator object, and sorts by most recent. """

		context = super().get_context_data(**kwargs)
		context['most_recent'] =  self.most_recent
		context['page_request_var'] = "page"
		context['queryset'] = self.queryset
		return context



class PostDetailView(DetailView):
	""" Individual post view  """
	model = News_Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		""" Specifies absolute URL for the object so it can be passed used as part of Delete and Update URLs. """

		obj = self.get_object()
		context = super().get_context_data(**kwargs)
		context['page_request_var'] = "page"
		obj.get_absolute_url()
		return context



class PostDeleteView(DeleteView):
	""" Deletes the post and brings you back to the main posts page after confirmation. """
	model = News_Post
	template_name = 'blog/delete_post.html'
	success_url = '/news_post'







