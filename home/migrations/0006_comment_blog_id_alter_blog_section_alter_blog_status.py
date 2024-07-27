# Generated by Django 5.0.7 on 2024-07-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_alter_blog_id_alter_blog_section_alter_blog_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="blog_id",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="blog",
            name="section",
            field=models.CharField(
                choices=[
                    ("Popular", "Popular"),
                    ("Recent", "Recent"),
                    ("Trending", "Trending"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="status",
            field=models.CharField(
                choices=[("1", "PUBLISH"), ("0", "DRAFT")], default=0, max_length=1
            ),
        ),
    ]