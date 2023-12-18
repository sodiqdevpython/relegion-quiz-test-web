from django.contrib import admin
from .models import Question, QuizModel, Answer, Result, GroupUNI, Profile, Theme


@admin.register(QuizModel)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'tugatish']

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_right']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'quiz','image_question']
    list_display = ['name', 'quiz','image_question']
    inlines = [AnswerInlineModel]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_right', 'question']

@admin.register(Result)
class ResultAdmiin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'total_question', 'corrent_question', 'total', 'create_at','id','quiz_id', 'spend_time']
    list_filter = ['quiz']

@admin.register(GroupUNI)
class AdminGroupUNI(admin.ModelAdmin):
    class Meta:
        list_display = ['name', 'overall_ball', 'group_students']
        search_fields = ['group_students']

@admin.register(Profile)
class AdminViewProfile(admin.ModelAdmin):
    class Meta:
        list_display = ['name', 'overall_ball', 'group_students']
        search_fields = ['user']

@admin.register(Theme)
class AdminViewTheme(admin.ModelAdmin):
    class Meta:
        list_display = ['title']
        search_fields = ['title']