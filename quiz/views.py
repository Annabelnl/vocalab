from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Score
from django.utils import timezone
import random

@login_required
def afficher_question(request):
    questions = list(Question.objects.all())
    questions_selectionnees = random.sample(questions, min(3, len(questions))) if questions else []
    
    for question in questions_selectionnees:
        options = [question.reponse_correcte] + eval(question.reponses_incorrectes)
        random.shuffle(options)
        question.options = options
    
    return render(request, 'quiz/question.html', {'questions': questions_selectionnees})

def verifier_reponse(request):
    if request.method == "POST":
        resultats = []
        erreurs = []  # Liste pour stocker les erreurs
        score = 0
        total_questions = len(request.POST.getlist("question_ids"))

        for question_id in request.POST.getlist("question_ids"):
            question = get_object_or_404(Question, id=question_id)
            reponse_utilisateur = request.POST.get(f"reponse_{question_id}")
            correcte = (reponse_utilisateur == question.reponse_correcte)
            if correcte:
                score += 1
            else:
                erreurs.append(question)  # Ajoute à la liste des erreurs si incorrect
            resultats.append({'question': question, 'correcte': correcte})

        pourcentage = (score / total_questions) * 100 if total_questions > 0 else 0
        pourcentage = round(pourcentage)

        Score.objects.create(
            user=request.user,
            score=score,
            total_questions=total_questions,
            pourcentage=pourcentage,
            date=timezone.now()
        )

        return render(request, 'quiz/resultat.html', {
            'resultats': resultats,
            'score': score,
            'total_questions': total_questions,
            'pourcentage': pourcentage,
            'erreurs': erreurs,  # Inclut la liste des erreurs dans le contexte
        })
    else:
        return redirect('afficher_question')

def signup(request):
    return render(request, 'signup.html')
