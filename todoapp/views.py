from django.shortcuts import render, redirect
# ログイン時のみアクセスできるようlogin_requiredをインポート
from django.contrib.auth.decorators import login_required
# 問3-5-1 変数 todo に Todo model のインスタンスを格納しましょう。また、Todo の import も行いましょう。
from .models import Todo
# 問3-5-4 accounts_app.models から CustomUser モデルを import して利用できるようにしましょう。
from accounts_app.models import CustomUser
# 問3-8 TodoForm を使えるように import を追加しましょう。
from .forms import TodoForm
# 問5-2 編集画面には クラスベースビュー を使用するので views.py で import しましょう。
from django.views.generic.edit import UpdateView
# 問5-3-4 django.urls から reverse_lazy を import しましょう。
from django.urls import reverse_lazy
# 問6-4-3 組み込みタグ date を datetime から import しましょう。
from datetime import date
# 問8-9 完了タスクの数が増えていくので、paginator を使い、ページ数制限をしましょう。paginator をインポートしましょう。
from django.core.paginator import Paginator

# ユーザー情報
@login_required
def user(request, num=1):
    print("★todoapp_user★")
    # 問2-5 user 関数の pass を削除しましょう。
    # pass
    # 問2-6 user 変数に user 情報を格納しましょう。request の user とすることでログイン時の user 情報が取得できます。
    user = request.user
    # 問3-9 from 変数に TodoForm インスタンスを格納しましょう。
    form = TodoForm()
    # 問4-3 Todo インスタンスの filterメソッドを使用して、現在ログイン中の user の id を検索して、Todo データを todos 変数に格納しましょう。
    todos = Todo.objects.filter(user_id=request.user.id)
    # 問4-4 今回は完了と未完了タスクを振り分けたいので、incomplete 変数に todos 変数の done(完了したかどうかのフラグ)が False のものを格納しましょう。未完了タスク(done=false)を変数incompleteしましょう。
    incomplete = todos.filter(done=False)
    # 問8-2 未完了タスクを期限(deadline)の近い順（早い）に並べ替えましょう。
    incomplete = incomplete.order_by('deadline')
    # 問8-3 未完了タスクの総数を count を使って todo_number に格納しましょう。同名で params にも追加して HTML に渡しましょう。
    todo_number = incomplete.count()
    # 問4-4 今回は完了と未完了タスクを振り分けたいので、完了タスク(done=True)を変数doneしましょう。
    done = todos.filter(done=True)
    # 問8-4 完了タスクを終了日（finished_date）の近い順（早い）に並べ替えましょう。
    done = done.order_by('finished_date')
    # 問8-5 done_number に完了タスクの総数を count を使って格納しましょう。同名で params にも追加して HTML に渡しましょう。
    done_number = done.count()
    # 問8-6 期限内(deadline)までに終了(finished_date)したタスクを計算するために、within が True のデータの数を count を使って、within 変数に格納しましょう。同名で params にも追加して HTML に渡しましょう。
    within = todos.filter(within=True).count()
    # 問8-7-1 もし期限内に完了した数(within)が 0 件、または完了タスクの総数(done_number)が 0 件の場合の条件式を追加しましょう。
    if within == 0 or done_number == 0 :
        # 問8-7-2 条件式がTureの場合、除算は error となるため、変数 ratio にあらかじめ 0 を代入しましょう。
        ratio = 0
    else:
        # 問8-7-3 条件式がFalseの場合、期限内に完了した数 ÷ 完了タスク数 ×100 を計算した値を ratio 変数に格納しましょう。
        ratio = within / done_number * 100
    # 問8-9 page 変数に Paginator オブジェクトを格納しましょう。完了のみページ機能をつけたいので第一引数には done、第二引数には 5 を設定しましょう。
    page = Paginator(done, 5)
    # 問8-10 現在のページを取得したいので、done 変数に page.get_page(num)を再代入しましょう。
    done = page.get_page(num)
    # 問8-8 今日の日付より前の期限タスクのタイトルを赤文字表示させたいので、today 変数に date.today()で本日の日付を格納しましょう。同名で params にも追加して HTML に渡しましょう。
    today = date.today()
    # 問2-7 params 変数(辞書型)を作成しましょう。
    params = {
        'user': user,
        'form': form,
        'done': done,
        'incomplete': incomplete,
        'todo_number': todo_number,
        'done_number': done_number,
        'ratio': ratio,
        'today': today,
        'within': within
    }
        # 問2-7 params に、キーを user、valueに user 変数を指定しましょう。

        # 問3-5-3 POST の deadline を todo インスタンスの deadline に設定しましょう。
        # 問3-10 辞書型で、keyに form という名前、valueに form 変数を、 params に 追加しましょう。

        # paginatorのオブジェクトから指定ページのレコードを取り出す

        # 問4-5 辞書型で、keyに done という名前、valueに done 変数を、 params に 追加しましょう。

        # 問4-6 辞書型で、keyに incomplete という名前、valueに incomplete 変数を、 params に 追加しましょう。

        # 問8-3 未完了タスクの総数を count を使って todo_number に格納しましょう。同名で params にも追加して HTML に渡しましょう。

        # 問8-5 done_number に完了タスクの総数を count を使って格納しましょう。同名で params にも追加して HTML に渡しましょう。

        # 問8-6 within 変数に within が True のデータの数を count を使って格納しましょう。同名で params にも追加して HTML に渡しましょう。

        # 問8-7-4 keyに ratio 、valueに ratio 変数を params に追加しましょう。

        # 問8-8 今日の日付より前の期限タスクのタイトルを赤文字表示させたいので、today 変数に date.today()で本日の日付を格納しましょう。同名で params にも追加して HTML に渡しましょう。


    # 問2-8 todoapp/index.html を表示させる render 関数を追加しましょう。第三引数には params を指定しましょう。
    return render(request, 'todoapp/index.html', params)

# タスクの追加処理
@login_required
def add(request):
    print("★add★")
    # 問3-4 add 関数の pass を削除しましょう。
    # pass
    # 問3-5 request の method が post の時の条件式を追加しましょう。
    if request.method == 'POST': 
        # 問3-5-1 変数 todo に Todo model のインスタンスを格納しましょう。また、Todo の import も行いましょう。
        todo = Todo()
        # 問3-5-2 POST の title を todo インスタンスの title に設定しましょう。
        todo.title = request.POST.get('title')
        # 問3-5-3 POST の deadline を todo インスタンスの deadline に設定しましょう。
        todo.deadline = request.POST.get('deadline')
        # 問3-5-5 todo インスタンスの user_id は、対象のCustomUser モデルの値を指定する必要があります。CustomUser モデルのObjectsを利用して、検索した値を取得して、todo インスタンスの user_idに格納しましょう。検索条件は、requestのuser_idを設定します。
        todo.user_id = CustomUser.objects.get(id=request.user.id)
        # 問3-5-6 save メソッドを使い、保存しましょう。
        todo.save()

    # 問3-6 条件式の外で urls.pyで定義したuser のページに遷移できるよう redirect を設定しましょう。
    return redirect('user')

# 問5-3 TodoUpdateView クラスを作成して、UpdateView を継承しましょう。コメントアウトを外しましょう。
class TodoUpdateView(UpdateView):
    print("★TodoUpdateView★")
    # 問5-3-1 model 変数に Todo を指定しましょう。model 変数には、編集データを登録する model を指定しましょう。
    model = Todo
    # 問5-3-2 fields 変数に title と deadline をリスト型で指定しましょう。fields には編集したい項目を追加できます。
    fields = ['title', 'deadline']
    # 問5-3-3 template_name_suffix 変数に \_update_form を追加しましょう
    # ※デフォルトでは[`model名`_form.html]となっているため、名称の変更
    template_name_suffix = '_update_form'
    # 問5-3-5 success_url 変数に reverse_lazy メソッドを利用して、name=user を指定したものを格納しましょう。※変更に成功した際の遷移先を設定。
    success_url = reverse_lazy('user')

@login_required
def done(request, num):
    print("★todoapp_done★")
    # 問6-3 pass を削除しましょう。
    # pass
    # 問6-4 num が True の時の条件文を作成しましょう。
    if num:
        # 問6-4-1 Todo オブジェクトから get メソッドを使用して、検索条件 pk=num でデータを取得した値を todo という変数に、格納しましょう。
        todo = Todo.objects.get(pk=num)
        # 問6-4-2 todo の中の done を True に変更しましょう。※該当タスクの終了フラグをtrueにする
        todo.done = True
        # 問6-4-4 終了日を本日になるように、todo の中の finished_date（終了日）に組み込みタグの date.today()を設定しましょう。
        todo.finished_date = date.today()
        # 問6-4-5 期限よりも終了日が早かった時に、todo の within フラグを True にする条件式を追加しましょう。
        if todo.deadline > date.today():
            todo.within = True
        # 問6-4-6 todo の save メソッドを使い、変更した内容を登録しましょう。
        todo.save()
    # 問6-5 条件文の外で user に redirect しましょう。
    return redirect('user')

@login_required
def delete(request, num):
    print("★todoapp_delete★")
    # 問7-3 pass を削除しましょう。
    # pass
    # 問7-4 num が True の時の条件文を作成しましょう。
    if num:
        # 問7-4-1 Todo オブジェクトから get メソッドを使用して、検索条件 pk=num でデータを取得した値を todo という変数に、格納しましょう。
        todo = Todo.objects.get(pk=num)
        # 問7-4-2 todo の delete メソッドを使い、選択したタスクを削除しましょう。
        todo.delete()
    # 問7-5 条件文の外で user に redirect しましょう。
    return redirect('user')

