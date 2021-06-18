from django import forms
from .models import Post,Category,Comment

choices=Category.objects.all().values_list('name','name')

choice_list=[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','body','category','header_image','status')

        widgets= {
            # 'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is a placeholder'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'author_id','type':'hidden'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'status':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','category','status','header_image')

        widgets= {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-select'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }