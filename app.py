# app.py (Phase 2 changes)
from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "replace_with_a_secure_random_key"

# 10 warriors (IDs 1—10; images currently placeholders)
warriors = [
    {"id": 1, "name": "Warrior 1", "image": "warrior1.png"},
    {"id": 2, "name": "Warrior 2", "image": "warrior2.png"},
    {"id": 3, "name": "Warrior 3", "image": "warrior3.png"},
    {"id": 4, "name": "Warrior 4", "image": "warrior4.png"},
    {"id": 5, "name": "Warrior 5", "image": "warrior5.png"},
    {"id": 6, "name": "Warrior 6", "image": "warrior6.png"},
    {"id": 7, "name": "Warrior 7", "image": "warrior7.png"},
    {"id": 8, "name": "Warrior 8", "image": "warrior8.png"},
    {"id": 9, "name": "Warrior 9", "image": "warrior9.png"},
    {"id": 10, "name": "Warrior 10", "image": "warrior10.png"}
]

@app.route("/", methods=["GET", "POST"])
def select_warrior():
    # On POST, store chosen warrior ID and redirect to /battle
    if request.method == "POST":
        chosen_id = int(request.form.get("warrior_id"))
        session["player_id"] = chosen_id
        return redirect(url_for("battle_placeholder"))
    # On GET, render selection screen
    return render_template("select.html", warriors=warriors)

@app.route("/battle")
def battle_placeholder():
    # Temporary placeholder until battle logic is implemented
    return "<h2>Battle route reached. (Coming soon…)</h2>"

if __name__ == "__main__":
    app.run(debug=True)
