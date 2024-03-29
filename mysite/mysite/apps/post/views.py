from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from .forms import NewPostForm
from .models import Comment, Post

# Create your views here.


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    '''
    Home View and Post View
    '''

    model = Post
    template_name = 'post/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    extra_context = {'value': 'Create Post'}
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # print(self.request.user)
        # print(Post.objects.all())
        commented = []
        if self.request.user.is_authenticated:
            # Logic to check all post commented by user
            for post in Post.objects.all():
                for comment in post.post_comment.all():
                    if self.request.user == comment.user:
                        commented.append(post)

            # Here I passed list of posts, liked(another logic applied later)
            # and commented according to loggedIn user.
            context['commented'] = commented
        return context


@method_decorator(login_required, name='dispatch')
class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = NewPostForm
    template_name = 'post/create_post.html'
    success_url = '/'
    success_message = 'Your Post Uploaded Successfully!'
    extra_context = {'value': 'Create'}

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.save(commit=False)
        form.instance.user_name = self.request.user
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        if post.post_comment.filter(user=self.request.user.id).exists():
            context['commented'] = [post]
        return context


@method_decorator(login_required, name='dispatch')
class LikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        # id = request.POST.get('sid') # it's a way to get data form ajax
        # print(id, post)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        # This calls likes_count() form model = Post
        count = post.likes_count()

        # This change is for ajax logic makes true if liked and vice versa
        is_like = not is_like

        return JsonResponse({'liked': is_like, 'count': count})


@method_decorator(login_required, name='dispatch')
class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = '/post/deleted/'
    # success_message = 'Your Post Deleted Successfully!'  # Not Working


@method_decorator(login_required, name='dispatch')
class PostUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'post/create_post.html'
    success_url = '/'
    extra_context = {'value': 'Update'}
    success_message = 'Your Post Updated Successfully!'


@method_decorator(login_required, name='dispatch')
class PostCommentView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        comment = Comment.objects.create(
            user=request.user, post=post, comment_text=request.POST['comment_text']
        )
        return JsonResponse(
            {
                'id': comment.id,
                'user': comment.user.username,
                'post': comment.post.id,
                'comment_text': comment.comment_text,
                'comment_count': post.post_comment.count(),
            }
        )
