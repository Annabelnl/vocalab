// Fonction pour afficher le hint
function showHint(questionId) {
    var hintElement = document.getElementById('hint_' + questionId);
    if (hintElement) {
        hintElement.style.display = 'block';
    }
}

// Fonction pour vérifier que chaque question a une réponse sélectionnée
function verifierReponses() {
    const form = document.getElementById('quiz-form');
    const questions = document.querySelectorAll('[name^="reponse_"]'); // Groupes de réponses pour chaque question
    let toutesRepondues = true;

    // Vérifier si chaque question a une réponse sélectionnée
    questions.forEach((questionGroup) => {
        const options = document.getElementsByName(questionGroup.name);
        const reponseSelectionnee = Array.from(options).some(option => option.checked);
        if (!reponseSelectionnee) {
            toutesRepondues = false;
        }
    });

    // Si des réponses manquent, afficher une confirmation
    if (!toutesRepondues) {
        const confirmer = confirm("Souhaitez-vous arrêter l'exercice ? Seules les bonnes réponses seront comptées.");
        if (!confirmer) {
            return false; // Empêche la soumission pour retour à l'exercice
        }
    }

    return true; // Soumet le formulaire si toutes les réponses sont complètes ou si l'utilisateur confirme l'arrêt
}