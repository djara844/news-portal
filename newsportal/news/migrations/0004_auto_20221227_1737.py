# Generated by Django 4.1.3 on 2022-12-27 17:37

from django.db import migrations
from news.models import News, Author, Category
import autoslug.fields


def add_news(apps, schema_editor):

    news = [
        {
            "title": "Refuerzos Premier league",
            "extract": "Estos son los refuerzos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=1p1fJucCTjgbb71U1dM21IN1hzRegmdoS",
            "content_image": "https://drive.google.com/uc?export=view&id=1p1fJucCTjgbb71U1dM21IN1hzRegmdoS",
            "is_active": True,
            "author_name_news": "Thanos",
            "category_name_news": "Premier League",
        },
        {
            "title": "Calendario Premier league",
            "extract": "Estos son los partidos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=1fgboOCzob-zVfuxjdldqvzSsmN0qWuIe",
            "content_image": "https://drive.google.com/uc?export=view&id=1fgboOCzob-zVfuxjdldqvzSsmN0qWuIe",
            "is_active": True,
            "author_name_news": "Otto",
            "category_name_news": "Premier League",
        },
        {
            "title": "Refuerzos Serie A",
            "extract": "Estos son los refuerzos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=1QhIJKbQk16gIbeZfXKcAcAZNwrPEILu8",
            "content_image": "https://drive.google.com/uc?export=view&id=1QhIJKbQk16gIbeZfXKcAcAZNwrPEILu8",
            "is_active": True,
            "author_name_news": "Leo",
            "category_name_news": "Serie A",
        },
        {
            "title": "Calendario Serie A",
            "extract": "Estos son los partidos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=1QhIJKbQk16gIbeZfXKcAcAZNwrPEILu8",
            "content_image": "https://drive.google.com/uc?export=view&id=1QhIJKbQk16gIbeZfXKcAcAZNwrPEILu8",
            "is_active": True,
            "author_name_news": "Thanos",
            "category_name_news": "Serie A",
        },
        {
            "title": "Refuerzos Liga Betplay",
            "extract": "Estos son los refuerzos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=1CbsxxuFdBTeyR34wxaYafWPyXVV2fZDX",
            "content_image": "https://drive.google.com/uc?export=view&id=1CbsxxuFdBTeyR34wxaYafWPyXVV2fZDX",
            "is_active": True,
            "author_name_news": "Otto",
            "category_name_news": "Liga Betplay",
        },
        {
            "title": "Calendario Liga Betplay",
            "extract": "Estos son los partidos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=1GjklfDVivJwg54TZlfQbFsngopRIhXjx",
            "content_image": "https://drive.google.com/uc?export=view&id=1GjklfDVivJwg54TZlfQbFsngopRIhXjx",
            "is_active": True,
            "author_name_news": "Leo",
            "category_name_news": "Liga Betplay",
        },
        {
            "title": "Refuerzos Bundesliga",
            "extract": "Estos son los refuerzos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=1CQuIyNrQf5PdlYfOVZJo0StmluzkLPoD",
            "content_image": "https://drive.google.com/uc?export=view&id=1CQuIyNrQf5PdlYfOVZJo0StmluzkLPoD",
            "is_active": True,
            "author_name_news": "Thanos",
            "category_name_news": "Bundesliga",
        },
        {
            "title": "Calendario Bundesliga",
            "extract": "Estos son los partidos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=1-5jvwj-Gbs1qXXKLdznfGhuom1oM7H2N",
            "content_image": "https://drive.google.com/uc?export=view&id=1-5jvwj-Gbs1qXXKLdznfGhuom1oM7H2N",
            "is_active": True,
            "author_name_news": "Otto",
            "category_name_news": "Bundesliga",
        },
        {
            "title": "Refuerzos Ligue 1",
            "extract": "Estos son los refuerzos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=1PYG-aoS3ClPwmP2G3WmxDrQAJ-DK42zP",
            "content_image": "https://drive.google.com/uc?export=view&id=1PYG-aoS3ClPwmP2G3WmxDrQAJ-DK42zP",
            "is_active": True,
            "author_name_news": "Leo",
            "category_name_news": "Ligue 1",
        },
        {
            "title": "Calendario Ligue 1",
            "extract": "Estos son los partidos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=1o-KRG7Oxk_sbAgUrEX-Z5Oo3VVTsPxaX",
            "content_image": "https://drive.google.com/uc?export=view&id=1o-KRG7Oxk_sbAgUrEX-Z5Oo3VVTsPxaX",
            "is_active": True,
            "author_name_news": "Thanos",
            "category_name_news": "Ligue 1",
        },
        {
            "title": "Refuerzos La Liga",
            "extract": "Estos son los refuerzos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=12D8_NcpeB4pg6tZKOaErADQtzFWKV7hl",
            "content_image": "https://drive.google.com/uc?export=view&id=12D8_NcpeB4pg6tZKOaErADQtzFWKV7hl",
            "is_active": True,
            "author_name_news": "Otto",
            "category_name_news": "La Liga",
        },
        {
            "title": "Calendario La Liga",
            "extract": "Estos son los partidos para la temporada 2023",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "cover_image": "https://drive.google.com/uc?export=view&id=19TF5grfuKHAzlXbeZp1ymWCmeRE_xXGu",
            "content_image": "https://drive.google.com/uc?export=view&id=19TF5grfuKHAzlXbeZp1ymWCmeRE_xXGu",
            "is_active": True,
            "author_name_news": "Leo",
            "category_name_news": "La Liga",
        },
    ]

    for news_item in news:
        author_news = Author.objects.get(name=news_item["author_name_news"])
        category_news = Category.objects.get(name=news_item["category_name_news"])
        new_news = News(
            title=news_item["title"],
            extract=news_item["extract"],
            content=news_item["content"],
            cover_image=news_item["cover_image"],
            content_image=news_item["content_image"],
            is_active=news_item["is_active"],
            author_id=(author_news.id),
            category_id=(category_news.id),
        )
        new_news.save()
        # new_news.author.add(author_news)
        # new_news.category.add(category_news)


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_auto_20221227_1737"),
    ]

    operations = [
        migrations.RunPython(add_news),
    ]
