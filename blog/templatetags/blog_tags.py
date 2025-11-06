from django import template
from ..models import Post
from django.db.models.query import QuerySet
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown


register = template.Library()


@register.simple_tag
def total_posts() -> int:
    """Возвращает общее количество опубликованных постов."""

    return Post.published.count()


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5) -> dict[str, QuerySet[Post]]:
    """Возвращает контекст для включения последних опубликованных постов в шаблон."""

    latest_posts = Post.published.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5) -> QuerySet[Post]:
    """Возвращает список постов с наибольшим количеством комментариев."""

    return (
        Post.published.annotate(total_comments=Count("comments"))
        .exclude(total_comments=0)
        .order_by("-total_comments")[:count]
    )


@register.filter(name="markdown")
def markdown_format(text: str) -> str:
    """Преобразует текст в HTML с использованием Markdown."""

    return mark_safe(markdown.markdown(text))
