from rest_framework import serializers
from app.models import Quiz, Question, Options, Submission, SubmissionExtra


class QuizListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ('id', 'title', 'start', 'end', 'duration')


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('id', 'option', )


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, source='options_set')

    class Meta:
        model = Question
        fields = ('id', 'title', 'options',)


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set')

    class Meta:
        model = Quiz
        fields = ('id', 'title', 'start', 'end', 'duration',
                  'questions', 'num_of_questions')


class SubmitedAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubmissionExtra
        fields = ('question', 'answer')


class SubmissionSerializer(serializers.ModelSerializer):
    answers = SubmitedAnswerSerializer(
        many=True, allow_null=False, allow_empty=False)

    class Meta:
        model = Submission
        fields = ('id', 'quiz', 'start', 'end', 'user', 'answers', 'marks')
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        answers = validated_data.pop('answers')
        submission = Submission.objects.create(user=user, **validated_data)
        submission_objs = [SubmissionExtra(submission=submission, question=answer['question'],
                                           answer=answer['answer'])
                           for answer in answers]
        SubmissionExtra.objects.bulk_create(submission_objs)
        return submission
