from . import views
from django.urls import path
# 問5-4 urls.py に TodoUpdateView を views から import しましょう。
from .views import TodoUpdateView

urlpatterns = [
    # 問2-9 urls.py に url を''、関数を user、ページ名を user として新しく path を追加しましょう。
    path('', views.user, name='user'),
    # index関数がnumというint型のページ番号をつけてアクセスできるようする
    path('<int:num>/', views.user, name='user'),
    # 問3-12 url を add/、name を add として、add 関数につながるパスを追加しましょう。
    path('add/', views.add, name='add'),
    # 問5-5 urls.py に url に update/<int:pk>、name に update を持ち、TodoUpdateView にアクセスできるパスを追加しましょう。
    path('update/<int:pk>', TodoUpdateView.as_view(), name='update'),
    # 問6-6 urls.py に done 関数への path を追加しましょう。url は done/<int:num>、name には done を指定しましょう。
    path('done/<int:num>', views.done, name='done' ),
    # 問7-6  urls.py に delete 関数への path を追加しましょう。url は delete/<int:num>、name には delete を指定しましょう。
    path('delete/<int:num>', views.delete, name='delete'),
]