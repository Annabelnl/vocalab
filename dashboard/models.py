from django.db import models
from django.conf import settings
from django.utils import timezone

class UserProgress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)
    quizzes_taken = models.IntegerField(default=0)
    average_score = models.FloatField(default=0.0)
    last_activity = models.DateTimeField(auto_now=True)
    badges = models.ManyToManyField('Badge', blank=True)

    def __str__(self):
        return f"Progression de {self.user.username}"

    def update_progress(self, new_score):
        """Méthode pour mettre à jour les progrès de l'utilisateur après chaque quiz."""
        self.total_score += new_score
        self.quizzes_taken += 1
        self.average_score = self.total_score / self.quizzes_taken
        self.last_activity = timezone.now()
        self.save()

class Badge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_awarded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class UserQuizHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.ForeignKey('quiz.Score', on_delete=models.CASCADE) 
    date_taken = models.DateTimeField(default=timezone.now)
    theme = models.CharField(max_length=100)
    success_rate = models.FloatField()


    def __str__(self):
        return f"Historique de {self.user.username} pour le quiz du {self.date_taken}"

    def get_score(self):
        from quiz.models import Score  # Import à l'intérieur de la méthode pour éviter le problème d'import circulaire
        return Score.objects.filter(user=self.user)

class UserGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal_description = models.CharField(max_length=255)
    target_date = models.DateTimeField()
    is_achieved = models.BooleanField(default=False)

    def __str__(self):
        return f"Objectif de {self.user.username} : {self.goal_description}"
