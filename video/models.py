from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Video(models.Model):
    video_id = models.IntegerField('视频ID')
    video_uuid = models.IntegerField()
    video_title = models.CharField()
    video_cover_url = models.CharField()
    video_category_id = models.CharField()
    video_url = models.CharField()
    video_label_id = models.CharField()
    video_brief = models.TextField()
    upload_user_id = models.IntegerField()
    upload_time = models.CharField()

    class Meta:
        # 模型类起一个更可读的名字一般定义为中文
        verbose_name = '视频类'
        # 模型的复数形式, 不定义会自动加在‘verbose_name’后‘s’
        verbose_name_plural = verbose_name


class SiteUser(models.Model):
    user_id = models.IntegerField()
    user_uuid = models.IntegerField()
    user_name = models.CharField()
    user_password = models.CharField()
    user_avatar_url = models.CharField()
    nickname = models.CharField()
    user_level = models.IntegerField()