from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model


class Quiz(TimeStampedModel):
    title = models.CharField(max_length=400, blank=False, null=False)
    start = models.DateTimeField(null=False, blank=False)
    end = models.DateTimeField(null=False, blank=False)

    @property
    def duration(self):
        return self.end-self.start

    @property
    def num_of_questions(self):
        return self.question_set.all().count()


class Question(TimeStampedModel):
    quiz = models.ForeignKey('app.Quiz', null=False, on_delete=models.CASCADE)
    title = models.TextField(null=False, blank=False)


class Options(TimeStampedModel):
    question = models.ForeignKey(
        'app.Question', null=False, on_delete=models.CASCADE)
    option = models.TextField(null=False, blank=False)
    is_correct = models.BooleanField(default=False)


class Submission(TimeStampedModel):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False)
    start = models.DateTimeField(null=False)
    end = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey('app.Quiz', on_delete=models.CASCADE, null=False)

    @property
    def marks(self):
        return self.submissionextra_set.filter(answer__is_correct=True).count()

    @property
    def answers(self):
        return self.submissionextra_set.all()


class SubmissionExtra(TimeStampedModel):
    submission = models.ForeignKey(
        'app.Submission', null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(
        'app.Question', null=False, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        'app.Options', null=False, on_delete=models.CASCADE)
