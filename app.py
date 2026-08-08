import os

from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "manasa-portfolio-key"
)

# ------------------------------
# EMAIL CONFIG
# ------------------------------

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")

mail = Mail(app)


# ------------------------------
# ROUTES
# ------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    msg = Message(
        subject=f"Portfolio Contact From {name}",
        sender=app.config["MAIL_USERNAME"],
        recipients=[app.config["MAIL_USERNAME"]],
        body=f"""
Name: {name}

Email: {email}

Message:
{message}
"""
    )

    msg.reply_to = email

    try:
        mail.send(msg)

        flash(
            "Your message has been sent successfully! "
            "I will get back to you soon."
        )

    except Exception as e:
        print("EMAIL ERROR:", e)

        flash(
            "Sorry, your message could not be sent. "
            "Please try again later."
        )

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)