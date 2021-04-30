from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, MovieShots, Actor, Ratting, RattingStar, Reviews

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):

    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="60"')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft", "id")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline, ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    readonly_fields = ("get_image",)
    form = MovieAdminForm
    # Gruparea cimpurilor din pagina de administrare
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"))
        }),
        (None, {
            "fields": ("year", "world_premiere", "country")
        }),
        (None, {
            "fields": (("actors", "directors", "genres", "category"), )
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"), )
        }),
        (None, {
            "fields": (("url", "draft", "trailer"), )
        }),

    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="200" height="200"')

    def unpublish(self, request, queryset):

        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 record was updated'
        else:
            message_bit = f"{row_update} records was updated"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):

        row_update = queryset.update(draft=True)
        if row_update == '1':
            message_bit = '1 record was updated'
        else:
            message_bit = f"{row_update} records was updated"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Publish"
    publish.allowed_permision = ('change', )

    unpublish.short_description = "Unpublish"
    unpublish.allowed_permision = ('change',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(Ratting)
class RattingAdmin(admin.ModelAdmin):
    list_display = ("movie", "ip")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="50" height="50"')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movies", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')


admin.site.register(RattingStar)

admin.site.site_title = "iWatch Movies"
admin.site.site_header = "iWatch Movies"

