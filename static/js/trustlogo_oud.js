// Détecter le protocole (https ou http)
var tlJsHost = (window.location.protocol == "https:") ? "https://secure.trust-provider.com/" : "http://www.trustlogo.com/";

// Créer dynamiquement une balise script pour charger TrustLogo
var scriptTag = document.createElement("script");
scriptTag.src = tlJsHost + "trustlogo/javascript/trustlogo.js";
scriptTag.type = "text/javascript";
document.body.appendChild(scriptTag);

// Une fois que le script est chargé, appeler TrustLogo pour afficher l'image du TrustLogo
scriptTag.onload = function() {
  TrustLogo("https://www.positivessl.com/images/seals/positivessl_trust_seal_sm_124x32.png", "POSDV", "none");
};
