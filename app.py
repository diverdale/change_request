import datetime
import os
import time

from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, TextAreaField,
                     SelectField)
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)

app.debug = True

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'outbound.cisco.com'

# toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)
mail = Mail(app)
Bootstrap(app)
Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summary')
def summary():
    changes = ChangeControl.query.all()
    print(changes)

    return render_template('summary.html', changes=changes)


@app.route('/change', methods=['GET', 'POST'])
def change():
    form = ChangeForm(request.form)

    # if request.method == 'POST' and form.validate(): This should work but it doesn't validate for some reason
    if request.method == 'POST':
        new_change = ChangeControl(change_type=form.change_type.data, title=form.title.data,
                                   swivel_desk=form.swivel_desk.data,
                                   owner_name=form.owner_name.data, start_date=form.start_date.data,
                                   end_date=form.end_date.data, summary=form.summary.data, vendor=form.vendor.data,
                                   technical_contact_email=form.technical_contact_email.data,
                                   implementation_plan=form.implementation_plan.data,
                                   rollback_plan=form.rollback_plan.data,
                                   test_plan=form.test_plan.data, impact=form.impact.data, urgency=form.urgency.data,
                                   failure_probability=form.failure_probability.data,
                                   network_impact_details=form.network_impact_details.data,
                                   justification=form.justification.data,
                                   emails=form.emails.data)
        message = {'change_type': form.change_type.data, 'title': form.title.data, 'owner_name': form.owner_name.data,
                    'swivel_desk': form.swivel_desk.data, 'technical_contact_email': form.technical_contact_email.data,
                    'implementation_plan': form.implementation_plan.data, 'rollback_plan': form.rollback_plan.data,
                    'test_plan': form.test_plan.data, 'justification': form.justification.data}
        db.session.add(new_change)
        db.session.commit()
        test_mail(message)
        return redirect(url_for('list'))
    return render_template('change.html', form=form)


@app.route('/list')
def list():
    changes = ChangeControl.query.all()
    print(changes)

    return render_template('list.html', changes=changes)

def test_mail(message):
    msg = Message("Change Request", sender="no-reply-flask@cisco.com",
                    recipients=["dalwrigh@cisco.com", "charleshenderson988@gmail.com"])
    msg.html = "<html>\
                <head>\
                    <style>\
                        td {border: 1px solid black;}\
                    </style>\
                <body style=\"background-color: #80aaff; min-height=400px;\">\
                <H1>Change Request Info</H1><br>\
                <table role=\"presentation\"style=\"border:1px solid black; border-collapse:collapse; width: 80%;\">\
                <tr style=\"background-color:#FFFFE0;\">\
                    <td><b>Change type</b></td>\
                    <td><b>Title</b></td>\
                    <td><b>Exclude Swivel Desk?</b></td>\
                </tr>\
                <tr>\
                    <td>" + message['change_type'] + "</td>\
                    <td>" + message['title'] + "</td>\
                    <td>" + message['swivel_desk'] + "</td>\
                </tr>\
                <tr style=\"background-color:#FFFFE0;\">\
                    <td><b>Owner/Implementor Name</b></td>\
                    <td colspan=\"2\"><b>Technical Contact Email</b></td>\
                </tr>\
                <tr>\
                    <td>" + message['owner_name'] + "</td>\
                    <td colspan=\"2\">" + message['technical_contact_email'] + "</td>\
                </tr>\
                <tr style=\"background-color:#FFFFE0;\">\
                    <td colspan=\"3\"><b>Implementation Plan</b></td>\
                </tr>\
                <tr>\
                    <td colspan=\"3\">" + message['implementation_plan'] + "</td>\
                </tr>\
                <tr style=\"background-color:#FFFFE0;\">\
                    <td colspan=\"3\"><b>Rollback Plan</b></td>\
                </tr>\
                <tr>\
                    <td colspan=\"3\">" + message['rollback_plan'] + "</td>\
                </tr>\
                <tr style=\"background-color:#FFFFE0;\">\
                    <td colspan=\"3\"><b>Test Plan</b></td>\
                </tr>\
                <tr>\
                    <td colspan=\"3\">" + message['test_plan'] + "</td>\
                </tr>\
                <tr style=\"background-color:#FFFFE0;\">\
                    <td colspan=\"3\"><b>Justification</b></td>\
                </tr>\
                <tr>\
                    <td colspan=\"3\">" + message['justification'] + "</td>\
                </tr>\
                </table>\
                </body>\
                </html>"
    mail.send(msg)

#@app.route('/send')
def send_mail(message):
    msg = Message("Update", sender="no-reply-flask@cisco.com",
                   recipients=["dalwrigh@cisco.com"])
    msg.body = "change type: " + message['change_type'] + " title: " + message['title'] + " owner: " + message['owner']
    mail.send(msg)

    for key,value in message.items():
        print(key, value)
         

class ChangeControl(db.Model):
    __tablename__ = 'change_control'

    id = db.Column(db.Integer, primary_key=True)
    change_number = db.Column(db.String(32))
    change_type = db.Column(db.String(64))
    title = db.Column(db.String(64))
    swivel_desk = db.Column(db.String(3))
    owner_name = db.Column(db.String(64))
    start_date = db.Column(db.String(64))
    end_date = db.Column(db.String(64))
    summary = db.Column(db.Text())
    vendor = db.Column(db.String(64))
    technical_contact_email = db.Column(db.String(64))
    implementation_plan = db.Column(db.Text())
    rollback_plan = db.Column(db.Text())
    network_impact_details = db.Column(db.Text())
    test_plan = db.Column(db.Text())
    impact = db.Column(db.String(20))
    urgency = db.Column(db.String(20))
    failure_probability = db.Column(db.String(20))
    justification = db.Column(db.Text())
    emails = db.Column(db.String(128))

    def __init__(self, change_number, change_type, title, swivel_desk, owner_name, start_date, end_date, summary,
                 vendor, technical_contact_email, implementation_plan, rollback_plan, network_impact_details,
                 test_plan, impact, urgency, failure_probability, justification, emails):
        self.change_number = change_number
        self.change_type = change_type
        self.title = title
        self.swivel_desk = swivel_desk
        self.owner_name = owner_name
        self.start_date = start_date
        self.end_date = end_date
        self.summary = summary
        self.vendor = vendor
        self.technical_contact_email = technical_contact_email
        self.implementation_plan = implementation_plan
        self.rollback_plan = rollback_plan
        self.network_impact_details = network_impact_details
        self.test_plan = test_plan
        self.impact = impact
        self.urgency = urgency
        self.failure_probability = failure_probability
        self.justification = justification
        self.emails = emails


class ChangeForm(FlaskForm):
    change_type = SelectField('Change Type', choices=[('Normal', 'Normal'), ('Standard', 'Standard'),
                                                      ('Emergency', 'Emergency')])
    title = StringField('Title', validators=[DataRequired()])
    swivel_desk = SelectField('Exclude SwivelDesk?', choices=[('yes', 'yes'), ('no', 'no')])
    owner_name = StringField('Owner/Implementor Name')
    vendor = StringField('Vendor')
    technical_contact_email = StringField('Technical Contact Email', validators=[Email()])

    start_date = DateTimeLocalField('Change Start', default=datetime.date.fromtimestamp(time.time()),
                                    format='%Y-%m-%dT%H:%M')
    end_date = DateTimeLocalField('Change End', default=datetime.date.fromtimestamp(time.time()),
                                  format='%Y-%m-%dT%H:%M')
    summary = TextAreaField('Summary', render_kw={"placeholder": "Input Description"})
    implementation_plan = TextAreaField('Implementaion Plan', render_kw={"placeholder": "Implementation Steps"})
    rollback_plan = TextAreaField('Rollback Plan', render_kw={"placeholder": "Rollback Steps"})
    test_plan = TextAreaField('Test Plan', render_kw={"placeholder": "Test Steps"})
    impact = SelectField('Impact', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    urgency = SelectField('Urgency', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    failure_probability = SelectField('Failure Probability', choices=[('Low', 'Low'), ('Medium', 'Medium'),
                                                                      ('High', 'High')])
    network_impact_details = TextAreaField('Network Impact Details', render_kw={"placeholder": "Network impact details"})
    justification = TextAreaField('Justification', render_kw={"placeholder": "Justification for Change"})
    emails = StringField('Additional Emails Needed', render_kw={"placeholder": "Separate with comma"})
    submit = SubmitField('Send')



if __name__ == '__main__':
    app.run()
