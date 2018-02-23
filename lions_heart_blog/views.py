from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Comment, CompanyInformation, Reviews
from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms import CommentForm, ReviewForm
from django.contrib import messages


class PostListView(ListView):
    model = Post
    template_name = 'lions_heart_blog/blog.html'
    paginate_by = 8


class PostDetailView(DetailView):
    model = Post
    template_name = 'lions_heart_blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CommentCreate(CreateView):

    model = Comment
    form_class = CommentForm
    template_name = 'lions_heart_blog/blog_detail.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.post = Post.objects.get(pk=self.kwargs['post_id'])
        obj.save()
        return HttpResponseRedirect(reverse('blog_detail', args=(self.kwargs['post_id'])))

    def get_success_url(self):
            return reverse('blog_detail', args=(self.kwargs['post_id']))


class AboutView(ListView):
    template_name = 'lions_heart_blog/about.html'
    model = CompanyInformation


class ContactView(ListView):
    template_name = 'lions_heart_blog/contacts.html'
    model = CompanyInformation


class ReviewsListView(ListView):
    model = Reviews
    template_name = 'lions_heart_blog/reviews.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewsListView, self).get_context_data(**kwargs)
        context['form'] = ReviewForm
        return context


class ReviewCreate(CreateView):

    model = Reviews
    form_class = ReviewForm

    def form_invalid(self, form):
        messages.error(self.request, 'Error. Please, try again.')
        return HttpResponseRedirect(reverse('reviews'))

    def get_success_url(self):
            return reverse('reviews')
