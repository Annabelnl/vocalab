import csv
from quiz.models import questions  # Assure-toi que le nom du modèle est correct

def run():
    with open('questions.csv', newline='', encoding='ISO-8859-1') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Passer la ligne d'en-tête
        for row in reader:
            # Vérifier que chaque colonne contient des données
            if len(row) < 5 or not all(row):
                print(f"Ligne incorrecte ou incomplète : {row}")  # Afficher les lignes incomplètes
                continue  # Passer cette ligne

            Question.objects.create(
                question=row[0],
                reponse_correcte=row[1],
                reponses_incorrectes=row[2],
                hint=row[3],
                explication=row[4],
            )
