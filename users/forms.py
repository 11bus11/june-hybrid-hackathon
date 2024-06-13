from django import forms
from users.models import User


class CustomSignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'social_security_no', 
                  'phone_no', 'address', 'post_code', 'city')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, request):
        user = super(CustomSignupForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.social_security_no = self.cleaned_data['social_security_no']
        user.phone_no = self.cleaned_data['phone_no']
        user.address = self.cleaned_data['address']
        user.post_code = self.cleaned_data['post_code']
        user.city = self.cleaned_data['city']
        user.save()
        return user

    def signup(self, request, user):
        pass
