from django.db import models
from django.conf import settings
from django.utils import timezone

class Theme(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    phrase = models.TextField()
    mot_cible = models.CharField(max_length=255, default="à définir")
    reponse_correcte = models.CharField(max_length=255)
    reponses_incorrectes = models.TextField()
    hint = models.TextField()
    explication = models.TextField()
    
    # Nouveau champ pour indiquer si la question est un cognate
    is_cognate = models.BooleanField(default=False, verbose_name="Cognate")

    # Nouveau champ pour le thème
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Question sur '{self.mot_cible}': {self.phrase}"

class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    theme = models.CharField(max_length=100)
    pourcentage = models.IntegerField()  # Champ pour le pourcentage de réussite
    date = models.DateTimeField(auto_now_add=True)  # Date et heure de la tentative
    interval_since_last_quiz = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Score: {self.score}/{self.total_questions} ({self.pourcentage}%)"

class UserError(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_wrong_answer = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Erreur de {self.user.username} sur la question '{self.question.phrase}'"
