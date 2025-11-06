from django.contrib.sitemaps import Sitemap
from .models import Post
from django.db.models.query import QuerySet
from datetime import datetime


class PostSitemap(Sitemap):
    """Карта сайта для публикаций."""

    changefreq = "weekly"
    priority = 0.9

    def items(self) -> QuerySet[Post]:
        """Возвращает QuerySet опубликованных публикаций, включаемых в карту сайта."""

        return Post.published.all()

    def lastmod(self, obj: Post) -> datetime:
        """Возвращает дату и время последнего изменения указанной публикации.
        Используется поисковой системой для отслеживания обновлённого контента."""

        return obj.updated
