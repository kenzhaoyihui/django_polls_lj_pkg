from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_texts']
    fieldsets = [
        ('Question information', {'fields': ['question_texts']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_texts', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
