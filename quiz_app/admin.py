from django.contrib import admin
from .models import (
    Quiz,
    Question,
    Answer,
    Result
)
# Register your models here.

admin.site.register(Quiz)
admin.site.register(Result)

class AnswerInLine(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
