from django.contrib import admin
from .models import VideoCategory, VideoLabel, Video, SiteUser


# Register your models here.


@admin.register(VideoCategory)
class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    list_display_links = ('category_name',)


@admin.register(VideoLabel)
class VideoLabelAdmin(admin.ModelAdmin):
    list_display = ('label_id', 'label_name')
    list_display_links = ('label_name',)


@admin.register(SiteUser)
class VideoSiteUser(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_password',
                    'user_avatar_url', 'nickname', 'user_level')
    list_display_links = ('user_name',)
    # 每页行数小于等于20页，超过则分页
    list_per_page = 20


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'video_cover_url',
                    'video_category_id', 'video_url', 'video_label_id',
                    'video_brief', 'upload_user_id', 'upload_time')
    list_display_links = ('video_title',)
    list_per_page = 20

    ordering = ('upload_time',)
    list_editable = ['upload_user_id']

    def video_category(self):
        return self.video_category_id.category_name

