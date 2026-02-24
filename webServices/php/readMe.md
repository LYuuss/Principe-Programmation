# Service Web - Implémentation d'un client  

Afin de mettre en oeuvre l'intéropérabilité, nous implémentons, en PHP, un client qui se chargera de lancer des requêtes au serveur fruitsBasket (voir repertoire apiRest) implémenté en PYTHON.  
Différent repertoire au sein de src/ :  
- Services : Class pour se charger des requetes
- View : Factoriser le code (affichage...), Ne plus mélanger la logique PHP et HTML   
- Assets : Styliser le code (CSS...)