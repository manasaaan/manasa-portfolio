import os
import requests

from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "manasa-portfolio-key"
)


# --------------------------------
# HOME
# --------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------
# CONTACT FORM
# --------------------------------

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    # Check whether Resend API key exists
    resend_api_key = os.environ.get("RESEND_API_KEY")

    if not resend_api_key:
        print("ERROR: RESEND_API_KEY is not configured.")
        flash("Sorry, the email service is not configured.")
        return redirect("/")

    # Email data
    data = {
        "from": "Portfolio <onboarding@resend.dev>",
        "to": ["manasanarayanaswami34@gmail.com"],
        "subject": f"Portfolio Contact From {name}",
        "reply_to": email,
        "text": f"""
Name: {name}

Email: {email}

Message:
{message}
"""
    }

    # Resend API headers
    headers = {
        "Authorization": f"Bearer {resend_api_key}",
        "Content-Type": "application/json"
    }

    try:

        response = requests.post(
            "https://api.resend.com/emails",
            json=data,
            headers=headers,
            timeout=15
        )

        print("RESEND STATUS:", response.status_code)
        print("RESEND RESPONSE:", response.text)

        if response.status_code in [200, 201]:

            flash(
                "Your message has been sent successfully! "
                "I will get back to you soon."
            )

        else:

            flash(
                "Sorry, your message could not be sent. "
                "Please try again later."
            )

    except requests.exceptions.RequestException as e:

        print("RESEND CONNECTION ERROR:", e)

        flash(
            "Sorry, your message could not be sent. "
            "Please try again later."
        )

    except Exception as e:

        print("EMAIL ERROR:", e)

        flash(
            "Sorry, your message could not be sent. "
            "Please try again later."
        )

    return redirect("/")


# --------------------------------
# RUN APPLICATION
# --------------------------------

if __name__ == "__main__":
    app.run(debug=True)