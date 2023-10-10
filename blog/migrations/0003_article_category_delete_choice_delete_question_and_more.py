# Generated by Django 4.2.5 on 2023-10-04 08:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_choice_question_delete_article_delete_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create time')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified time')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='title')),
                ('body', mdeditor.fields.MDTextField(verbose_name='article content')),
                ('pub_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='publish time')),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='d', max_length=1, verbose_name='article status')),
                ('article_order', models.IntegerField(default=0, verbose_name='order by larger num')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create time')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified time')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='category name')),
                ('index', models.IntegerField(default=0, verbose_name='order by larger num')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='category'),
        ),
    ]
