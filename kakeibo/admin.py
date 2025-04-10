from django.contrib import admin #Djangoの管理機能のインポート
from .models import Category, Record #kakeibo/models.pyから関数をインポート


@admin.register(Category) #Django管理画面でCategoryモデルを管理する
class CategoryAdmin(admin.ModelAdmin): #管理画面用のクラス
    list_display = ('name', 'type') #管理画面の一覧を指定
    list_filter = ('type',) #フィルターの選択肢を追加


@admin.register(Record) #Django管理画面でRecordモデルを管理
class RecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'date', 'created_at')
    list_filter = ('user', 'category', 'date')
    search_fields = ('memo',)
