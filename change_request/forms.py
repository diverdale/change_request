from flask_wtf import FlaskForm
import datetime, time
from wtforms import (StringField, SubmitField, TextAreaField,
                     SelectField)
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, Email


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
    network_impact_details = TextAreaField('Network Impact Details',
                                           render_kw={"placeholder": "Network impact details"})
    justification = TextAreaField('Justification', render_kw={"placeholder": "Justification for Change"})
    emails = StringField('Additional Emails Needed', render_kw={"placeholder": "Separate with comma"})
    submit = SubmitField('Send')

