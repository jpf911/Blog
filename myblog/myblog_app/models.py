from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from datetime import datetime,date

class Category(models.Model):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['id']

    name=models.CharField(max_length=255,verbose_name=_('Category'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category')

class Profile(models.Model):
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        ordering = ['id']

    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE,verbose_name=_('User'))
    profile_pic= models.ImageField(null=True,blank=True,upload_to='images/profile/',verbose_name=_('Profile Picture'))
    bio=models.TextField(null=True,blank=True,verbose_name=_('Bio'))

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['id']

    title= models.CharField(max_length=255,verbose_name=_('Post Title'))
    header_image= models.ImageField(null=True,blank=True,upload_to='images/',verbose_name=_('Image'))
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_('Author'))
    body=RichTextField(blank=True,null=True,verbose_name=_('Description'))
    status = models.BooleanField(default=False,verbose_name=_('Private'))
    post_date=models.DateTimeField(auto_now_add=True,verbose_name=_('Date Posted'))
    category= models.CharField(max_length=255,verbose_name=_('Category'))
    likes= models.ManyToManyField(User,related_name='blog_posts',verbose_name=_('Likes'))

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return '%s | %s' % (self.title, self.author)

    def get_absolute_url(self):
        # return reverse('article-details',args=(str(self.id)))
        return reverse('home')

class Comment(models.Model):
    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ['id']

    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE,verbose_name=_('Post Comment'))
    name=models.CharField(max_length=255,verbose_name=_('Correspondent'))
    body=models.TextField(verbose_name=_('Comment'))
    date_added=models.DateTimeField(auto_now_add=True,verbose_name=_('Date Commented'))

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
