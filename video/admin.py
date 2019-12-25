from django.contrib import admin
from .models import VideoCategory, VideoLabel, Video, SiteUser

# Register your models here.


class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    list_display_links = ('category_name',)


class VideoLabelAdmin(admin.ModelAdmin):
    list_display = ('label_id', 'label_name')
    list_display_links = ('label_name',)


class VideoSiteUser(admin.ModelAdmin):
    list_display = ('user_id', 'user_uuid', 'user_name', 'user_password',
                    'user_avatar_url', 'nickname', 'user_level')
    list_display_links = ('user_name',)
    # 每页行数小于等于20页，超过则分页
    list_per_page = 20


class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_uuid', 'video_title', 'video_cover_url',
                    'video_category_id', 'video_url', 'video_label_id',
                    'video_brief', 'upload_user_id', 'upload_time')
    list_display_links = ('video_title', )
    list_per_page = 20
    ordering = ('upload_time',)


admin.site.register(VideoCategory, VideoCategoryAdmin)
admin.site.register(VideoLabel, VideoLabelAdmin)
admin.site.register(SiteUser, VideoSiteUser)
admin.site.register(Video, VideoAdmin)
