from django.contrib.auth.models import User
from django.db import models
from DjangoUeditor.models import UEditorField
import uuid


# Create your models here.
# 视频类别表
class VideoCategory(models.Model):
    category_id = models.UUIDField('类别id',
                                   primary_key=True,
                                   auto_created=True,
                                   default=uuid.uuid4,
                                   editable=False)
    category_name = models.CharField('类别名称', max_length=30)


# 视频标签表
class VideoLabel(models.Model):
    label_id = models.IntegerField('标签id',
                                   primary_key=True,
                                   auto_created=True,
                                   default=uuid.uuid4,
                                   editable=False)

    label_name = models.CharField('标签名称', max_length=30)


# 用户表
class SiteUser(models.Model):
    user_id = models.UUIDField('用户id',
                               primary_key=True,
                               auto_created=True,
                               default=uuid.uuid4,
                               editable=False)
    user_uuid = models.IntegerField('uuid')
    user_name = models.CharField('账号', max_length=20)
    user_password = models.CharField('密码', max_length=10)
    # 'null=True' 允许该字段为空
    user_avatar_url = models.CharField('头像url', max_length=500, null=True)
    nickname = models.CharField('昵称', max_length=20)
    user_level = models.IntegerField('用户等级', default=0)


# 视频表
class Video(models.Model):
    video_id = models.UUIDField('视频id',
                                primary_key=True,
                                auto_created=True,
                                default=uuid.uuid4,
                                editable=False)
    video_uuid = models.IntegerField('uuid')
    video_title = models.CharField('标题', max_length=50)
    video_cover_url = models.CharField('封面图片url', max_length=500)
    video_category = models.ForeignKey(VideoCategory, on_delete=models.DO_NOTHING, null=True)
    video_url = models.CharField('视频url', max_length=500)
    video_label_id = models.ForeignKey(VideoLabel, on_delete=models.DO_NOTHING, null=True)
    video_brief = UEditorField('视频简介', width=800, height=500, toolbars='full',
                               imagePath='images/', filePath='source/',
                               upload_settings={'imageMaxSize': 1204000},
                               settings={}, command=None, blank=True)
    upload_user_id = models.IntegerField('用户id')
    upload_time = models.DateTimeField('上传时间', auto_now_add=True)

    # class Meta:
    #     # 模型类起一个更可读的名字一般定义为中文
    #     verbose_name = '视频类'
    #     # 模型的复数形式, 不定义会自动加在‘verbose_name’后‘s’
    #     verbose_name_plural = verbose_name





