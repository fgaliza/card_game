from apps.utils.abstract_models import BaseModel, models


class Card(BaseModel):

    name = models.CharField(max_length=64, unique=True)
    power = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('power',)

    @property
    def weaker_than(self):
        return Card.objects.filter(power__gt=self.power)

    @property
    def stronger_than(self):
        return Card.objects.filter(power__lt=self.power)

    @property
    def as_strong_as(self):
        return Card.objects.filter(power=self.power).exclude(name=self.name)
