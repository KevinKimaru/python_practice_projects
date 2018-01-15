from django.contrib import admin

from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

# class QestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

class ChoiceInline(admin.TabularInline):#StackedInline/TabularInline
    model = Choice
    extra = 3

class QestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QestionAdmin)


