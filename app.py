from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "manasa-portfolio-key"

# ------------------------------
#   EMAIL CONFIG
# ------------------------------

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "manasanarayanaswami34@gmail.com"     # your email
app.config['MAIL_PASSWORD'] = "xyug rdew pmxb efqq"              # paste app password

mail = Mail(app)

# ------------------------------
#   ROUTES
# ------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Create email message
    msg = Message(
        subject=f"Portfolio Contact From {name}",
        sender=email,
        recipients=["manasanarayanaswami34@gmail.com"],   # Your inbox
        body=f"""
        Name: {name}
        Email: {email}
        Message:
        {message}
        """
    )

    mail.send(msg)
    flash("Your message has been sent successfully! I will get back to you soon.")
    return redirect("/")  # back to home


if __name__ == "__main__":
    app.run(debug=True)
