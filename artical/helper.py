
import time
from urllib.parse import urlparse

from newspaper import Article
from newspaper.configuration import Configuration
from newspaper.exceptions import ArticleException


def extract_article(url):
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        raise ValueError("Invalid article URL.")

    config = Configuration()
    config.browser_user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    )
    config.request_timeout = (10, 30)
    config.fetch_images = False
    config.max_summary_sent = 3

    article = Article(url, config=config)

    for attempt in range(3):
        try:
            article.download()
            article.parse()
            break
        except ArticleException as exc:
            if attempt == 2:
                raise ValueError(
                    f"Unable to download article after 3 attempts: {exc}"
                ) from exc

            time.sleep(2 * (attempt + 1))

    if not article.text.strip():
        raise ValueError("The website did not provide article content.")

    article.nlp()

    return {
        "company_name": (
            article.meta_site_name or parsed.hostname
        ),
        "title": article.title,
        "url": article.url,
        "content": article.text,
        "category": ", ".join(article.meta_keywords or []),
        "summary": article.summary or article.meta_description,
        "published_at": article.publish_date,
    }


def get_category():
    return "Finace"


def get_summary():
    return "IT"


def extract_dummy_article(url):
    num = random.randint(10,99)
    return {
        "company_name": f"dummy name : company{num}",
        "title": f"dummy name : company{num}",
        "url": url,
        "content": f"dummy name : company{num}",
        "category": get_category(),
        "summary": get_summary(),
        "published_at": "01-01-2026",
    }
