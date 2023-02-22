from flask import Flask, render_template


app = Flask(__name__)


class GalileonMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route("/second-page/")
def hello_world_fancy():
    return render_template("second_page.html")


@app.route("/expressions/")
def hello_world():

    # interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    # addition and substraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # string concatenation
    first_name = "Captain"
    last_name = "Marvel"


    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name
    }

    return render_template("expressions.html", **kwargs)


@app.route("/data-structures/")
def render_data_structures():

    movies =[
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    car = {
        "brand": "Tesla",
        "model": "Roadster",
        "year": "2020"
    }

    moons = GalileonMoons("Io", "Europe", "Ganymede", "Casllisto")

    kwargs = {
        "movies": movies,
        "car": car,
        "moons": moons
    }

    return render_template("data_structures.html", **kwargs)


@app.route("/conditionals-basics/")
def render_conditionals():
    company = "Microsoft"
    return render_template("conditionals_basics.html", company=company)


@app.route("/for-loop/")
def render_loops_for():

    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]

    planets = {
        "Mercury": "Mercury",
        "Venus": "Venus",
        "Earth": "Earth",
        "Mars": "Mars",
        "Jupiter": "Jupiter",
        "Saturn": "Saturn",
        "Uranus": "Uranus",
        "Neptune": "Neptune"
    }

    return render_template("for_loop.html", planets=planets)

@app.route("/for-loop/conditionals/")
def render_for_loop_conditionals():
    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Jose Salvatierra": "Windows"
    }

    return render_template("loops_and_conditionals.html", user_os=user_os)