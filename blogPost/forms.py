from django import forms 
from .models import contactme,Post

class contact(forms.ModelForm):
    class Meta:
        model = contactme
        fields='__all__'


class createpost(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','content','image']
        
        title=forms.CharField(widget=forms.CharField),
        
        
        
       
        
        
    
    

