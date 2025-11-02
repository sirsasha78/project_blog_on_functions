from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.urls import reverse


class PublishedManager(models.Manager):

    def get_queryset(self) -> QuerySet["Post"]:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(
        max_length=255, unique_for_date="publish", verbose_name="URL"
    )
    body = models.TextField(verbose_name="Контент")
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name="Статус",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", verbose_name="Автор"
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        db_table = "post"
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", verbose_name="Статья"
    )
    name = models.CharField(max_length=80, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта")
    body = models.TextField(verbose_name="Комментарий")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания комментария"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления комментария"
    )
    active = models.BooleanField(default=True, verbose_name="Активность комментария")

    class Meta:
        db_table = "comment"
        ordering = ["created"]
        indexes = [
            models.Index(fields=["created"]),
        ]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self) -> str:
        return f"Комментарий {self.name} к посту {self.post}"
