from . import db


class ChangeControl(db.Model):
    __tablename__ = 'change_control'

    id = db.Column(db.Integer, primary_key=True)
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

    def __init__(self, change_type, title, swivel_desk, owner_name, start_date, end_date, summary,
                 vendor, technical_contact_email, implementation_plan, rollback_plan, network_impact_details,
                 test_plan, impact, urgency, failure_probability, justification, emails):
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

