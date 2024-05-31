from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username")
    password = forms.CharField(max_length=30, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=30, label="Paswod confirm", widget=forms.PasswordInput)
    
    
    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirm"]
        
        
        if password and confirm and password != confirm:
            raise forms.ValidationError("sifreler eyni deyil!!")
            
        values = {
            "username":username, 
            "password":password
        }
        return values
    
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username")
    password = forms.CharField(max_length=30, label="Password", widget=forms.PasswordInput)

class PhoneForm(forms.Form):
    phone = forms.CharField(max_length=30, label="Phone number", widget=forms.TextInput)
            
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone:
            raise forms.ValidationError("Phone number field is required")
        return phone

