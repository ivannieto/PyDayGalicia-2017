# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import

import numpy as np
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from pydaygal.configurations.models import Option
from pydaygal.utils.emails import send_email


class Review(TimeStampedModel):
    """A review assignation. A review user have assigned a proposal to
    review."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="reviews")
    proposal = models.ForeignKey("proposals.Proposal", related_name="reviews")

    relevance = models.PositiveIntegerField(
        verbose_name=_("Relevancia"), null=True, blank=True, help_text=_("Puntuación del 1 al 10")
    )
    interest = models.PositiveIntegerField(
        verbose_name=_("Interés General"), null=True, blank=True, help_text=_("Puntuación del 1 al 10")
    )
    newness = models.PositiveIntegerField(
        verbose_name=_("Novedad"), null=True, blank=True, help_text=_("Puntuación del 1 al 10")
    )

    notes = models.TextField(verbose_name=_("Notas del revisor"), blank=True, null=True)

    conflict = models.BooleanField(verbose_name=_("¿Existe un conflico de intereses?"), default=False)
    finished = models.BooleanField(verbose_name=_("¿Revisión finalizada?"), default=False)

    class Meta:
        unique_together = ["user", "proposal"]

    @property
    def avg_property(self):
        return self.avg()

    def avg(self):
        data = [self.relevance, self.interest, self.newness]
        weights = [
            Option.objects.get_value("{}_weights".format(name), 1.0) for name in ("relevance", "interest", "newness")
            ]
        if None not in data:
            data = zip(data, weights)
            return sum([attr * weight for attr, weight in data]) / sum(weights)
        return None

    def notify(self):
        context = {
            "site": Site.objects.get_current(),
            "first_name": self.user.first_name,
            "title": self.proposal.title,
        }
        send_email(
            context=context,
            template="emails/reviewers/new.html",
            subject=_("[%s] Tienes una nueva propuesta para revisar") % settings.CONFERENCE_TITLE,
            to=self.user.email,
            from_email="%s <%s>" % (settings.CONFERENCE_TITLE, settings.CONTACT_EMAIL)
        )

    def save(self, **kwargs):
        is_insert = self.pk is None
        old_user = None
        if not is_insert:
            old_user = Review.objects.get(pk=self.pk).user
        super(Review, self).save(**kwargs)
        if is_insert or self.user != old_user:
            self.notify()


class Reviewer(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="reviewer")

    def reviews_count(self):
        return self.user.reviews.count()

    def num_reviews(self):
        return Review.objects.filter(user=self.user).count()

    def mean(self):
        values = []
        for review in Review.objects.filter(user=self.user):
            values.append(review.relevance or 0)
            values.append(review.interest or 0)
            values.append(review.newness or 0)

        return np.mean(values)

    def std(self):
        values = []
        for review in Review.objects.filter(user=self.user):
            values.append(review.relevance or 0)
            values.append(review.interest or 0)
            values.append(review.newness or 0)

        return np.std(values)
