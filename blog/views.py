from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import CommentModelForm
from .models import BlogPostModel, CommentModel


class BlogListView(ListView):
    model = BlogPostModel
    template_name = 'main/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = BlogPostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')
        if tag:
            return qs.filter(tags__title=tag)
        return qs


class BlogDetailView(DetailView):
    model = BlogPostModel
    template_name = 'main/blog_detail.html'
    context_object_name = 'post'


class BlogCommentView(CreateView):
    form_class = CommentModelForm

    def get_success_url(self):
        return reverse('blogs:blog_comment', kwargs={'pk': self.kwargs.get('pk')})
