from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

# Register your models here.
#admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #The fields attribute lists just those fields that are to be displayed on the form, in order.
    #displayed vertically by default, but will display horizontally if you further group them in a tuple
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author') # Add display_genre
    inlines = [BooksInstanceInline]



#admin.site.register(Book, BookAdmin)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','id', 'status', 'due_back')
    list_filter = ('book','id', 'status', 'due_back')
