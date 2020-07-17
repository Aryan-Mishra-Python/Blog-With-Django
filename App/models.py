from django.db import models
import django
from django.core.urlresolvers import reverse


###########################
# Create your models here.#
###########################

# The Post Model~Database
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    post = models.TextField()
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    publication_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publication_date = django.utils.timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


# The Comment Model~Database
class Comment(models.Model):
    post = models.ForeignKey("App.Post", related_name='comments')
    author = models.CharField(max_length=150, blank=False, null=False)
    comment = models.CharField(max_length=10000)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.comment
