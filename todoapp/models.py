from django.db import models
from django.contrib.auth import get_user_model

class Todo(models.Model):
    # todoの件名
    title = models.CharField(max_length=100)
    # 期限
    deadline = models.DateField()
    # 作成日、auto_now_addの引数をTrueとすることで作成した際に自動で日付が入力される
    created_date = models.DateField(auto_now_add=True)
    # 更新日、auto_nowの引数をTrueとすることで変更した際に自動で日付が入力される
    update_date = models.DateField(auto_now=True)
    # 完了日
    finished_date = models.DateField(null=True,blank=True)
    # 完了したかどうかのフラグ、defaultでFalseが入る
    done = models.BooleanField(default=False)
    # 期限内に終わったかどうかのフラグ
    within = models.BooleanField(default=False)
    # ユーザーとの紐付け
    user_id = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)