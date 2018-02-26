from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Comment, CompanyInformation, Reviews
from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms import CommentForm, ReviewForm
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.utils.dateformat import DateFormat
from django.http import JsonResponse
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


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

    def form_valid(self, form):
        response_data = {'error': ''}
        obj = form.save(commit=False)
        obj.save()
        response_data['name'] = obj.author
        response_data['review'] = obj.review
        response_data['created'] = DateFormat(obj.created).format('d-m-Y')
        response_data['key'] = CaptchaStore.generate_key()
        response_data['image_url'] = captcha_image_url(response_data['key'])
        return JsonResponse(response_data)

    def form_invalid(self, form):
        response_data = {'name': '', 'review': '', 'created': ''}
        response_data['key'] = CaptchaStore.generate_key()
        response_data['image_url'] = captcha_image_url(response_data['key'])
        response_data['error'] = _('Error. Please, try again.')
        return JsonResponse(response_data)

