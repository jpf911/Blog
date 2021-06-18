from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView,LoginView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .forms import SignUpForm,EditProfileForm,PasswordChangingForm
from myblog_app.models import Profile,Post,Category


# def Posts(request):
#     posts = Post.objects.filter(author=request.user).order_by('-post_date')
#     return render(request, 'registration/posts.html', {'posts': posts})

class Posts(ListView):
    model = Post
    template_name='registration/posts.html'
    cats= Category.objects.all()
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        post = Post.objects.all()
        context = super(Posts, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        context['post'] = post
        return context

def UserLoginView(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match!',})
        else:
            login(request, user)
            # return redirect('home')
            return render(request,'home.html')


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'edit_profile_page.html'
    fields = ['user','profile_pic','bio']
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model= Profile
    template_name='registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/password_success.html')

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name='registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name='registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user