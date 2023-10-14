from django.db import models
# AbstractUser を継承してカスタムユーザーを作成するためにインポート
from django.contrib.auth.models import AbstractUser

# 問1-8 AbstractUserを継承して、CustomUserテーブルを作成する
class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    email = None
    last_login = None
    is_superuser = None
    is_staff = None