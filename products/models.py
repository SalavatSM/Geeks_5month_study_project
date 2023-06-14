from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    is_hit = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def category_name(self):
        # try:
        #     return self.category.name
        # except:
        #     return 'No category'
        return self.category.name if self.category else 'No category'

    @property
    def tags_name(self):
        return [tag.name for tag in self.tags.all()]

    @property
    def reviews(self):
        return self.product_reviews.filter(stars__gt=3)


STAR_CHOICES = (
    (1, '* '),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* '),
)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews')
    stars = models.IntegerField(default=5, choices=STAR_CHOICES)

    def __str__(self):
        return self.text
