from django import forms          # anytime you want to put something into data base from the frontend then we need to use forms in django
from .models import PostModel, Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    
    # meta needs atleast one parameter
    class Meta:
        model = PostModel
        fields = ('title','content')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title','content')


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',widget=forms.TextInput(attrs={'placeholder': 'Add comment here...'}))
    class Meta:
        model = Comment
        fields = ('content',)

