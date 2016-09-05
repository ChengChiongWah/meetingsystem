# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
   
class meeting_meeting(osv.Model):
    _name = "meeting.meeting"

    _columns = {
        "meeting name" : fields.char("Meeting Name", required=True, size=64),
        "meeting type" : fields.char("Meeting Type", required=True,),
        "start date" : fields.date("Start Date"),
        "expiration date" : fields.date("Expiration Date"),
        "numbers" : fields.integer("Numbers"),
        "email" : fields.char("Email"),
        "meetingroom id" : fields.many2one("meeting.room", "MeetingRoom Id", required=True,),
        "organizer" : fields.many2one("res.users", "Organizer", required=True,),
        "meeting summary" : fields.text("Meeting Summary"),
    }

class meeting_room(osv.Model):
    _name = "meeting.room"

    _columns = {
        "meetingroom id" : fields.integer("Room ID", required=True,),
        "meetingroom size" : fields.float("Room Size"),
        "equipment" : fields.char("Equipment"),
        "seats max" : fields.integer("Seats_Max", required=True,),
        "location" : fields.char("Location", required=True,),
        "meetingroom name" : fields.char("MeetingRoom Name", required=True,),
        }
