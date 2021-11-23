from flask_mail import Message
from . import mail


def send_mail(message):
    msg = Message("Change Request", sender="no-reply-flask@cisco.com",
                  recipients=["dalwrigh@cisco.com"])
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
