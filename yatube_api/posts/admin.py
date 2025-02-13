from django.contrib import admin
from posts.models import Comment, Follow, Group, Post


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Админка для групп."""
    list_display = ('id', 'title', 'slug', 'description')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Админка для постов."""
    list_display = ('id', 'text', 'author', 'pub_date', 'group')
    list_filter = ('pub_date', 'author', 'group')
    search_fields = ('text', 'author__username')
    raw_id_fields = ('author',)
    ordering = ('-pub_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Админка для комментариев."""
    list_display = ('id', 'text', 'author', 'post', 'created')
    list_filter = ('created', 'author', 'post')
    search_fields = ('text', 'author__username', 'post__text')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Админка для подписок."""
    list_display = ('id', 'user', 'following')
    search_fields = ('user__username', 'following__username')
    list_filter = ('user', 'following')
