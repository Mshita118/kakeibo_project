from django.db import models #django.db.modelsを使ってテーブルをオブジェクトとして利用
from django.contrib.auth.models import User #Djangoのユーザー認証を定義する


class Kakeibo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ユーザーごとのデータ管理
    date = models.DateField()  # 日付
    category = models.CharField(max_length=50)  # カテゴリ（食費・交通費など）
    description = models.CharField(max_length=200, blank=True)  # メモ
    amount = models.IntegerField()  # 金額（整数）

    def __str__(self):
        return f'{self.date} - {self.category}: {self.amount}円'



class Category(models.Model): #DBのテーブルを定義
    name = models.CharField(max_length=50) #カテゴリの名前を表示するフィールドを定義
    TYPE_CHOICES = ( #選択肢を定義するタプル
        ('income', '収入'),
        ('expense', '支出'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES) #カテゴリのタイプを定義。choices=TYPE_CHOICESで選択肢を制限


    def __str__(self): #オブジェクトを文字列として表現する特殊関数
        return f"{self.name} ({self.get_type_display()})"


class Record(models.Model): #DBのテーブルの定義
    user = models.ForeignKey(User, on_delete=models.CASCADE) #ユーザーと関連付ける。on_delete=models.CASCADEでユーザーが削除された場合、記録も削除される
    category = models.ForeignKey(Category, on_delete=models.PROTECT) #on_delete=models.PROTECTにより、カテゴリが削除されてもレコードは残る
    amount = models.DecimalField(max_digits=10, decimal_places=2) #金額管理のフィールド。計算精度の為に、DecimalFieldを使用
    date = models.DateField() #取引日。収支の記録
    memo = models.TextField(blank=True, null=True) #メモフィールド。blank=True, null=Trueで空でも登録が可能になる
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.category.name} - ¥{self.amount}"
