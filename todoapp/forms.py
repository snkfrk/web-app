from django import forms
# 問3-2-2 models から Todoモデルを import しましょう。
from .models import Todo
# 問9-6 bootstrap のカレンダービューを import しましょう。
from bootstrap_datepicker_plus.widgets import DatePickerInput

# 問3-2 Form を作成しましょう。名前を TodoForm とし、引数には modelForm を渡しましょう。
class TodoForm(forms.ModelForm):
    # 問3-2-5 TodoForm 内のdef __init__関数のコメントアウトを外しましょう。
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # ラベル末尾の:(コロン)をなくす
        self.label_suffix = " "
        for field in self.fields.values():
            # 入力欄の初期値(placeholder)をそれぞれのfieldのlabelに設定する
            field.widget.attrs['placeholder'] = field.label
            # labelを非表示にする
            field.label = ''
    # 問3-2-1 Meta クラスを作成しましょう。
    class Meta:
        # 問3-2-2 model には Todo を選択しましょう。
        model = Todo
        # 問3-2-3 作成時に使うフィールドは title と deadline のみなので、fields にリスト型で指定しましょう。
        fields = ['title','deadline']
        # 問3-2-4 ラベルを設定するため、辞書型で値を格納します。labels 変数に title にはタスク名、deadline には期限というように指定しましょう。
        labels = {'title':'タスク名','deadline':'期限'}
        # 問9-7 TodoForm の Meta クラスに widgets を追加しましょう。期限(deadline)のfieldをbootstrapを使ってカレンダービューしましょう。
        widgets = {
            'deadline': DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            'title':forms.TextInput(attrs={'style': 'width:400px'}),
        }