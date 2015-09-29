# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import utils.file
import utils.db.fields
import utils.db.utils


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', utils.db.fields.BigAutoField(primary_key=True, serialize=False)),
                ('address1', models.CharField(max_length=128)),
                ('address2', models.CharField(default='', blank=True, max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=16)),
                ('post_code', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', blank=True, max_length=63, unique=True)),
                ('description', models.CharField(default='', blank=True, max_length=127)),
                ('tags', models.CharField(default='', blank=True, max_length=2048)),
                ('parent', models.ForeignKey(blank=True, to='alatting_website.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', utils.db.fields.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=2048)),
                ('parent', utils.db.fields.BigForeignKey(blank=True, to='alatting_website.Comment', related_name='children', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=utils.db.utils.generate_uuid, max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', utils.db.fields.OverWriteImageField(storage=utils.file.OverwriteStorage(), width_field='width', height_field='height', upload_to=utils.file.get_image_path)),
                ('width', models.PositiveSmallIntegerField(blank=True)),
                ('height', models.PositiveSmallIntegerField(blank=True)),
                ('format', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=utils.db.utils.generate_uuid, max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', utils.db.fields.OverWriteFileField(storage=utils.file.OverwriteStorage(), upload_to=utils.file.get_music_path)),
                ('format', models.CharField(default='mp3', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user', models.OneToOneField(db_column='id', primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('gender', models.CharField(default='unknown', max_length=15, choices=[('Unknown', 'Unknown'), ('Male', 'Male'), ('Female', 'Female')])),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', utils.db.fields.BigAutoField(primary_key=True, serialize=False)),
                ('unique_name', models.CharField(max_length=512, unique=True)),
                ('url', models.CharField(max_length=512)),
                ('logo_title', models.CharField(max_length=512)),
                ('short_description', models.CharField(max_length=1024)),
                ('phone', models.CharField(max_length=16)),
                ('mobile', models.CharField(default='', blank=True, max_length=16)),
                ('email', models.EmailField(default='', blank=True, max_length=254)),
                ('lifetime_type', models.CharField(default='specific', max_length=15, choices=[('weekly', 'weekly'), ('specific', 'specific')])),
                ('lifetime_value', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=15, choices=[('Draft', 'Draft'), ('Published', 'Published'), ('Active', 'Active'), ('Inactive', 'Inactive')])),
                ('width', models.PositiveSmallIntegerField(default=800)),
                ('height', models.PositiveSmallIntegerField(default=1024)),
                ('views_count', models.IntegerField(default=0)),
                ('likes_count', models.IntegerField(default=0)),
                ('comments_count', models.IntegerField(default=0)),
                ('forwarded_count', models.IntegerField(default=0)),
                ('reviews_score', models.SmallIntegerField(default=0)),
                ('html', utils.db.fields.OverWriteFileField(storage=utils.file.OverwriteStorage(), upload_to=utils.file.get_html_path)),
                ('css', utils.db.fields.OverWriteFileField(storage=utils.file.OverwriteStorage(), upload_to=utils.file.get_css_path)),
                ('script', utils.db.fields.OverWriteFileField(storage=utils.file.OverwriteStorage(), upload_to=utils.file.get_script_path)),
                ('tags', models.CharField(default='', blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PosterImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=63)),
                ('image', models.ForeignKey(related_name='poster_images', to='alatting_website.Image')),
            ],
        ),
        migrations.CreateModel(
            name='PosterLike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PosterVideo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.CharField(default=utils.db.utils.generate_uuid, max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', utils.db.fields.OverWriteFileField(storage=utils.file.OverwriteStorage(), upload_to=utils.file.get_video_path)),
                ('format', models.CharField(default='mp4', max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityInvitation',
            fields=[
                ('poster', utils.db.fields.BigOneToOneField(parent_link=True, primary_key=True, to='alatting_website.Poster', serialize=False)),
                ('activity_status', models.CharField(default='coming', max_length=15, choices=[('coming', 'coming'), ('now', 'now'), ('finished', 'finished'), ('cancelled', 'cancelled')])),
                ('invitation_message', models.CharField(max_length=512)),
                ('activity_start_time', models.DateTimeField()),
                ('activity_end_time', models.DateTimeField()),
                ('special_description', models.CharField(default='', blank=True, max_length=1024)),
                ('activity_reminder_message', models.CharField(default='', blank=True, max_length=1024)),
                ('parking_notice_message', models.CharField(default='', blank=True, max_length=1024)),
                ('accepted_count', models.IntegerField(default=0)),
                ('rejected_count', models.IntegerField(default=0)),
                ('need_pre_notification', models.BooleanField(default=True)),
                ('pre_minutes_to_notify', models.IntegerField(default=0)),
            ],
            bases=('alatting_website.poster',),
        ),
        migrations.CreateModel(
            name='BusinessMarketing',
            fields=[
                ('poster', utils.db.fields.BigOneToOneField(parent_link=True, primary_key=True, to='alatting_website.Poster', serialize=False)),
                ('slogan', models.CharField(default='', blank=True, max_length=128)),
                ('parking_notice_message', models.CharField(default='', blank=True, max_length=1024)),
                ('need_reservation', models.BooleanField(default=True)),
                ('business_keywords', models.CharField(default='', blank=True, max_length=512)),
            ],
            bases=('alatting_website.poster',),
        ),
        migrations.CreateModel(
            name='ExpertShow',
            fields=[
                ('poster', utils.db.fields.BigOneToOneField(parent_link=True, primary_key=True, to='alatting_website.Poster', serialize=False)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('sex', models.CharField(max_length=10, choices=[('male', 'male'), ('female', 'female')])),
                ('birthday', models.DateField(blank=True, null=True)),
                ('profession', models.CharField(max_length=128)),
                ('working_years', models.IntegerField()),
                ('degree', models.CharField(max_length=64, choices=[('Bachelor', 'Bachelor'), ('Master', 'Master'), ('PHD', 'PHD')])),
                ('university', models.CharField(default='', blank=True, max_length=128)),
                ('awards', models.CharField(default='', blank=True, max_length=2048)),
                ('experince_description', models.CharField(max_length=2048)),
                ('industry', models.CharField(max_length=128)),
                ('specials', models.CharField(default='', blank=True, max_length=1024)),
                ('available_hours', models.CharField(default='', blank=True, max_length=64)),
                ('need_reservation', models.BooleanField(default=False)),
                ('expert_keywords', models.CharField(default='', blank=True, max_length=512)),
                ('parking_notice_message', models.CharField(default='', blank=True, max_length=512)),
                ('resume', utils.db.fields.OverWriteFileField(blank=True, storage=utils.file.OverwriteStorage(), upload_to='', null=True)),
            ],
            bases=('alatting_website.poster',),
        ),
        migrations.CreateModel(
            name='ProductSell',
            fields=[
                ('poster', utils.db.fields.BigOneToOneField(parent_link=True, primary_key=True, to='alatting_website.Poster', serialize=False)),
                ('price', models.FloatField(default=0)),
                ('is_negotiable', models.BooleanField(default=False)),
                ('is_express_delivery', models.BooleanField(default=False)),
                ('size_length', models.IntegerField(default=0)),
                ('size_width', models.IntegerField(default=0)),
                ('size_height', models.IntegerField(default=0)),
                ('is_product_available', models.BooleanField(default=False)),
                ('is_product_on_sale', models.BooleanField(default=False)),
                ('appearance_description', models.CharField(default='', blank=True, max_length=1024)),
                ('material_description', models.CharField(default='', blank=True, max_length=32)),
                ('color', models.CharField(default='', blank=True, max_length=32)),
            ],
            bases=('alatting_website.poster',),
        ),
        migrations.AddField(
            model_name='postervideo',
            name='poster',
            field=utils.db.fields.BigForeignKey(related_name='poster_videos', to='alatting_website.Poster'),
        ),
        migrations.AddField(
            model_name='postervideo',
            name='video',
            field=models.ForeignKey(related_name='poster_videos', to='alatting_website.Video'),
        ),
        migrations.AddField(
            model_name='posterlike',
            name='poster',
            field=utils.db.fields.BigForeignKey(to='alatting_website.Poster'),
        ),
        migrations.AddField(
            model_name='posterlike',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posterimage',
            name='poster',
            field=utils.db.fields.BigForeignKey(related_name='poster_images', to='alatting_website.Poster'),
        ),
        migrations.AddField(
            model_name='poster',
            name='address',
            field=utils.db.fields.BigForeignKey(related_name='posters', to='alatting_website.Address'),
        ),
        migrations.AddField(
            model_name='poster',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='poster',
            name='logo_image',
            field=models.ForeignKey(related_name='poster_logo_images', to='alatting_website.Image'),
        ),
        migrations.AddField(
            model_name='poster',
            name='main_category',
            field=models.ForeignKey(related_name='main_posters', to='alatting_website.Category'),
        ),
        migrations.AddField(
            model_name='poster',
            name='music',
            field=models.ForeignKey(blank=True, to='alatting_website.Music', null=True),
        ),
        migrations.AddField(
            model_name='poster',
            name='sub_category',
            field=models.ForeignKey(related_name='sub_posters', to='alatting_website.Category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='poster',
            field=utils.db.fields.BigForeignKey(to='alatting_website.Poster'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='postervideo',
            unique_together=set([('poster', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='posterlike',
            unique_together=set([('poster', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='posterimage',
            unique_together=set([('poster', 'name')]),
        ),
    ]
