from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(None)
    author_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f" {self.author_id.first_name} {self.author_id.last_name} "


class Invitation(models.Model):
    email = models.EmailField(unique=True, null=True)
    accepted = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.email}: {self.accepted}"


class Shaker(models.Model):
    shaker_name = models.CharField(max_length=50, null=True)
    owner = models.IntegerField(null=True)
    user_in_shake = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.shaker_name}: {self.owner}"


class Pairs(models.Model):
    user_1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_1"
    )
    user_2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_2"
    )
    shaker = models.ForeignKey(Shaker, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_1", "shaker"],
                name="unique_migration_host_combination",
            )
        ]

    def __str__(self):
        return f"{self.user_1} with {self.user_2} in shaker {self.shaker}"

    def return_user_2(self):
        return self.user_2
