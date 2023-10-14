from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
# 問1-9 django の UserCreaitonForm という modelform をインポートしましょう。
from django.contrib.auth.forms import UserCreationForm


# 問1-10 UserCreationForm を継承して SignupForm を作成しましょう。
class SignupForm(UserCreationForm):

    # 問1-10-1 Meta クラスを作成して、model に CustomUser を選択しましょう。
    class Meta:
        model = CustomUser

        # 問1-10-2 fields 変数にリスト型で username,password1,password2 を格納しましょう。
        fields = ['username', 'password1', 'password2']

    # 問1-10-3 def __init__関数のコメントアウトを外しましょう。
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.label_suffix = ''
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

# ユーザ名とパスワードで認証するフォームを作成できる
class LoginForm(AuthenticationForm):
    # ログインフォーム
    # 会員登録フォームと同様に、全てのフォームのclass属性に「form-control」・プレースホルダーを設定する
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['style'] = 'form-control'