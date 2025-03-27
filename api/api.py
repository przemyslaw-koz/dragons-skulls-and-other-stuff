import os

from flask import Flask, render_template

from repository.tiny_db_repo import TinyDBWorldRepository

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(project_root, "templates"),
    static_folder=os.path.join(project_root, "static"),
)
repo = TinyDBWorldRepository("db/world.json")


@app.route("/")
def game_index():
    return render_template("index.html")


@app.route("/start", methods=["GET"])
def start_game():
    return render_template("character_creation.html")


@app.route("/location/<loc_id>/npcs", methods=["GET"])
def list_npcs(loc_id):
    npcs = repo.get_npcs(loc_id)
    return npcs


@app.route("/location/<loc_id>", methods=["GET"])
def get_location(loc_id):
    location = repo.get_location(loc_id)

    location_data = {
        "id": loc_id,
        "name": location["name"],
        "description": location["desc"],
    }
    return render_template("partials/location.html", location=location_data)


@app.route("/location/<loc_id>/map", methods=["GET"])
def get_location_map(loc_id):
    location = repo.get_location(loc_id)

    location_map = {
        "id": loc_id,
        "name": location["name"],
        "map_options": location["options"],
    }
    return render_template("partials/map.html", location=location_map)


@app.route("/location/<loc_id>/options", methods=["GET"])
def list_directions(loc_id):
    return "list of possible directions in " + loc_id + " location"


@app.route("/location/<loc_id>/items", methods=["GET"])
def list_items(loc_id):
    return "list od items in " + loc_id + " location"


# @app.route("/location/<loc_id>/npcs/<npc_name>/<question>")
# def ask_question(loc_id, npc_name, question):
#    return "shows question and response - q: " + question + " l: " +
#
#
app.run(host="0.0.0.0", port=5000)
