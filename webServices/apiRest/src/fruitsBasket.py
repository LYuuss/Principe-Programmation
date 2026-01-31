from flask import Flask, jsonify, request

#   Creer l'app
app = Flask(__name__)

# liste des paniers 
#database_names = []
# liste de panier de fruits
database_basket = {}

universal_panier_fruit = [
    {"name":"apple", "color":"green", "from":"Spain"},
    {"name":"banana", "color":"yellow", "from":"Costa Rica"},
    {"name":"strawberry", "color":"red", "from":"France"},
]

database_basket["universalBasket"] = universal_panier_fruit

hiver_panier_fruit = [
    {"name":"kiwi", "color":"green", "from":"China"},
    {"name":"lemon", "color":"yellow", "from":"Russia"},
    {"name":"pear", "color":"green", "from":"Mongolia"}]

database_basket["winterBasket"] = hiver_panier_fruit

ete_panier_fruit = [
    {"name":"raspberry", "color":"red", "from":"Greece"},
    {"name":"watermelon", "color":"red", "from":"Algeria"},
    {"name":"apricot", "color":"yellow", "from":"Spain"}
]

database_basket["summerBasket"]= ete_panier_fruit

printemps_panier_fruit = [
    {"name":"grapefruit", "color":"magenta red", "from":"Barbados"},
    {"name":"lime", "color":"green", "from":"Venezuela"},
    {"name":"plum", "color":"dark red", "from":"Georgia"}
]

database_basket["springBasket"] = printemps_panier_fruit

database_names = list(database_basket.keys())
s1 = "La variété de paniers sont consultable en ajoutant '/nom_du_panier' au chemin actuelle. \n"
s2 = "Les différents noms de paniers sont : " + str(database_names)

@app.route("/")

def home():
    return "Vous êtes chez le primeurs, ajouter '/offers' pour consulter le catalogue de panier proposé\n"

# instruction pour consulter les paniers
@app.route("/offers", methods=["GET"])
def show_offer():
    return s1 + s2

# Affiche panier selon nom
@app.route("/offers/<string:name>", methods=["GET"])
def show_basket(name):
    if not database_basket[name]:
        return "Error aucun panier ne porte ce nom"
    return database_basket[name]

# Activer mode Debug pour voir les erreurs et recharger automatiquement le serveur 
if __name__ == '__main__':
    app.run(debug=True)
