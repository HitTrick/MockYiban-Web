# Generated by Django 3.1.2 on 2020-10-17 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='未命名', max_length=40, verbose_name='名字')),
                ('content', models.TextField(default='', verbose_name='内容')),
                ('contact_info', models.CharField(default='', max_length=40, verbose_name='联系方式')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_out', models.CharField(default='出', max_length=10, verbose_name='进/出')),
                ('name', models.CharField(default='未命名', max_length=20, verbose_name='学生名字')),
                ('stu_id', models.CharField(default='200000000', max_length=40, verbose_name='学号')),
                ('gate', models.CharField(default='南门', max_length=20, verbose_name='校门')),
            ],
        ),
    ]
