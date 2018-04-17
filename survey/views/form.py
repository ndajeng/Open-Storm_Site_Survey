"""Open-Storm site survey form main view"""
import flask
import survey


@survey.app.route("/", methods=["GET", "POST"])
def show_form():
    """Defines server-side action for survey form"""

    # Print returned information from the form
    if flask.request.method == "POST":
        print(flask.request.form)

    # Return survey template
    return flask.render_template("form.html")
