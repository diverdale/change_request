from flask import render_template, request, Blueprint, redirect, url_for
from .models import ChangeControl
from .forms import ChangeForm
from .utils import send_mail
from . import db

change_request = Blueprint('change_request', __name__)


@change_request.route('/')
def index():
    return render_template('index.html')


@change_request.route('/summary')
def summary():
    changes = ChangeControl.query.all()
    print(changes)

    return render_template('summary.html', changes=changes)


@change_request.route('/list_all')
def list_all():
    changes = ChangeControl.query.all()
    return render_template('list.html', changes=changes)


@change_request.route('/change', methods=['GET', 'POST'])
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
        # send_mail(message)
        return redirect(url_for('change_request.list_all'))
    return render_template('change.html', form=form)
