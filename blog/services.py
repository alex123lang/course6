from django.core.cache import cache

from blog.models import BlogArticle
from config.settings import CACHE_ENABLED


def get_articles_from_cache():
    if not CACHE_ENABLED:
        return BlogArticle.objects.all()
    else:
        key = 'categories_list'
        articles = cache.get(key)
        if articles is not None:
            return articles
        else:
            articles = BlogArticle.objects.all()
            cache.set(key, articles)
            return articles
