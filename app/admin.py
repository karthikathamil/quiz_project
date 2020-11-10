from django.contrib import admin
import nested_admin
from .models import Quiz,Question,Options,Submission

class Options(nested_admin.NestedTabularInline):
    model = Options
    extra = 4
    max_num = 4

class QuestionOptions(nested_admin.NestedTabularInline):
    model = Question
    inlines = (Options,)
    extra = 0

class QuizQuestions(nested_admin.NestedModelAdmin):
    inlines = (QuestionOptions,)


admin.site.register(Quiz, QuizQuestions)