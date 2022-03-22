from django import forms

from blog.models import BlogPost


class BlogPostForms(forms.ModelForm):
    class Meta:
        Model = BlogPost
        fields = "__all__"
