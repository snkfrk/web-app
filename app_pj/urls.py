from django.contrib import admin
# includeは、urls.pyと紐付けたいときに使えるメソッド
from django.urls import include
# pathは、ルーティングする（どのページを表示するかという指示を出す）メソッド
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(URL, include(紐付けたいurls.py))
    path('', include('todoapp.urls')),
    path('accounts_app/', include('accounts_app.urls')),
]
