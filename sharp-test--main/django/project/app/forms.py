from app.models import Answer

class corans(forms.ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"

class UserInfo(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"