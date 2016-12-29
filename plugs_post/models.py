from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from plugs_core import mixins

class Post(mixins.Timestampable, mixins.Slugable, models.Model):
    """
    Post model
    """
    name = models.CharField(max_length=100)
    text = models.TextField()
    section = models.ForeignKey('PostSection', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

    def __str__(self):
        """
        Python3 string representation
        """
        return self.name

    @property
    def slug_source(self):
        return self.name

    # pylint: disable=R0903
    class Meta:
        """
        Providing verbose names is recommended if
        we want to use i18n in admin site
        """
        verbose_name = _("post")
        verbose_name_plural = _("posts")


class PostSection(mixins.Timestampable, mixins.Slugable, models.Model):
    """
    Post Section model
    """
    name = models.CharField(max_length=100)
    description = models.CharField(
        max_length=255,
        help_text='Short description of the type of contents to be published in this section.',
        null=True, blank=True)

    def __str__(self):
        """
        Python3 string representation
        """
        return self.name

    @property
    def slug_source(self):
        return self.name

    # pylint: disable=R0903
    class Meta:
        """
        Providing verbose names is recommended if
        we want to use i18n in admin site
        """
        verbose_name = _("post section")
        verbose_name_plural = _("post sections")
