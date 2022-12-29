from django.db import models
from autoslug import AutoSlugField


# Create your models here.


class Author(models.Model):
    """
    A class to represent a Author, it is related to the News model by means of id

    ...

    Attributes
    _ _ _ _ _ _
    name : str
        name of author

    image : image
        image of author

    slug : str
        slug of author

    is_active : bool
        state of author, True or False

    create_at : date
        date of creation author

    update_at : date
        date of update author

    """

    name = models.CharField(
        "Nombre", 
        max_length=200, 
        blank=True
    )

    image = models.ImageField(
        max_length=255, 
        upload_to=None, 
        height_field=None, 
        width_field=None
    )

    slug = AutoSlugField(
        null=True, 
        default=None, 
        unique=True, 
        populate_from="name", 
        max_length=200
    )

    is_active = models.BooleanField(
        default=True
    )

    create_at = models.DateTimeField(
        "fecha de creación", 
        auto_now_add=True
    )

    update_at = models.DateTimeField(
        "fecha de actualización", 
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Category(models.Model):
    """
    A class to represent a Category, it is related to the News model by means of id

    ...

    Attributes
    _ _ _ _ _ _
    name : str
        name of author

    cover_image : image
        image cover of category

    description : str
        text description of category

    slug : str
        slug of category

    is_active : bool
        state of category, True or False

    create_at : date
        date of creation category

    update_at : date
        date of update category

    """

    name = models.CharField(
        "Nombre", 
        max_length=200, 
        blank=True
    )

    cover_image = models.ImageField(
        max_length=255, 
        upload_to=None, 
        height_field=None, 
        width_field=None
    )

    description = models.CharField(
        "Descripción", 
        max_length=1200, 
        blank=True
    )

    slug = AutoSlugField(
        null=True, 
        default=None, 
        unique=True, 
        populate_from="name", 
        max_length=200
    )

    is_active = models.BooleanField(
        default=True
    )

    create_at = models.DateTimeField(
        "fecha de creación", 
        auto_now_add=True
    )

    update_at = models.DateTimeField(
        "fecha de actualización", 
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class News(models.Model):
    """
    A class to represent a News, it is related to the News and Category Model's

    ...

    Attributes
    _ _ _ _ _ _
    title : str
        title of news

    extract : str
        short text of the news

    content : str
        content of news

    cover_image : image
        image for cover news

    content_image : image
        image for content news

    slug : str
        slug of news

    is_active : bool
        state of news, True or False

    create_at : date
        date of creation news

    update_at : date
        date of update news
    """

    title = models.CharField(
        "Título", 
        max_length=200, 
        blank=True
    )

    extract = models.CharField(
        "Extracto", 
        max_length=300, 
        blank=True
    )

    content = models.CharField(
        "Contenido", 
        max_length=1200, 
        blank=True
    )

    cover_image = models.ImageField(
        max_length=255,
        upload_to=None,
        height_field=None,
        width_field=None,
    )

    content_image = models.ImageField(
        max_length=255,
        upload_to=None,
        height_field=None,
        width_field=None,
    )

    slug = AutoSlugField(
        null=True, default=None, unique=True, populate_from="title", max_length=200
    )

    is_active = models.BooleanField(
        default=True
    )

    author = models.ForeignKey(
        Author,
        verbose_name="Autor",
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        Category,
        verbose_name="Categoría",
        on_delete=models.CASCADE,
    )

    create_at = models.DateTimeField(
        "fecha de creación", 
        auto_now_add=True
    )

    update_at = models.DateTimeField(
        "fecha de actualización", 
        auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
