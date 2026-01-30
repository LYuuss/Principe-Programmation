from flask import Flask, jsonify, request

#   Creer l'app
app = Flask(__name__)

# liste de fruit
panier_fruit = [
    {"name":"apple", "color":"green", "from":"Spain"},
    {"name":"banana", "color":"yellow", "from":"Costa Rica"},
    {"name":"strawberry", "color":"red", "from":"France"},
]

print(panier_fruit)

@app.route("/")

def home():
    return "Vous êtes chez le primeurs, ajouter /basket au chemin pour voir le contenue du panier du jour"

@app.route("/basket", methods=["GET"])
def show_basket():
    return jsonify(panier_fruit)

# Activer mode Debug pour voir les erreurs et recharger automatiquement le serveur 
if __name__ == '__main__':
    app.run(debug=True)
