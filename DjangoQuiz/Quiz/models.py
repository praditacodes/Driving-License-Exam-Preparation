from django.db import models
from django.contrib.auth.models import User

# Profile model to extend the default User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


# Quiz model to represent a collection of questions
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# QuesModel to store quiz questions and options
class QuesModel(models.Model):
    question = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    image = models.ImageField(upload_to='signals/', null=True, blank=True)  # Stores signal images

    def __str__(self):
        return self.question


# QuizResult model to store results for a specific user and quiz
class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)  # Referencing the Quiz model
    score = models.IntegerField()
    correct_answers = models.IntegerField()  # Track correct answers
    incorrect_answers = models.IntegerField()  # Track incorrect answers
    percentage = models.FloatField()  # Track percentage score
    total_questions = models.IntegerField()  # Total number of questions
    time_taken = models.FloatField()  # Time taken in seconds
    taken_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.quiz.title} - Score: {self.score}'
