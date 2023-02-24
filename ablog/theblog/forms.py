from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
  choice_list.append(item)

#hard code category choices, 
#choices= [('coding', 'Kitchen'), ('sports', 'sports'), ('entertainment', 'entertainment'),]
#this is python list and we need to add 2 fields one is original and other is its replacement. Now in the widgets field below add choices=choices before attrs.

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'title_tag', 'author','category', 'body', 'snippet', 'header_image')

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      #'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is title placeholder'}),
      # to place a brief description of the field
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'elder', 'type':'hidden'}),
      #'author': forms.Select(attrs={'class': 'form-control'}),
      'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      'snippet': forms.Textarea(attrs={'class': 'form-control'}),
    }


class EditForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title','title_tag','body', 'snippet')
    #removed ' 'author',' from fields field to remove author from update post page.
    

    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),
      #'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is title placeholder'}),
      # to place a brief description of the field
      'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
      #'author': forms.Select(attrs={'class': 'form-control'}),
      'body': forms.Textarea(attrs={'class': 'form-control'}),
      'snippet': forms.Textarea(attrs={'class': 'form-control'}),
    }