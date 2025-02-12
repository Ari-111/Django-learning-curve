from django.contrib import admin
from django.contrib import admin
from .models import Question,Choice

admin.site.site_header = "Polls management Admin"




class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            (None, {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
        
        list_display = ('question_text', 'pub_date', 'was_published_recently')
        list_filter = ['pub_date']
        search_fields = ['question_text']
inlines = [ChoiceInline]


admin.site.register(Question)



  # Makes Question model visible in admin panel


# Register your models here.
