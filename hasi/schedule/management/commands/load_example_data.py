from django.core.management.base import NoArgsCommand

from django.core.management.color import no_style

class Command(NoArgsCommand):
    help = "Load some sample data into the db"

    def handle_noargs(self, **options):
        import datetime
        from schedule.models import Calendar
        from schedule.models import Event
        from schedule.models import Rule

        print "checking for existing data ..."
        try:
            cal = Calendar.objects.get(name="E-Metering")
            print "It looks like you already have loaded this sample data, quitting."
            import sys
            sys.exit(1)
        except Calendar.DoesNotExist:
            print "Sample data not found in db."
            print "Install it..."


        print "Create Example Calendar ..."
        cal = Calendar(name="E-metering",slug="emetering")
        cal.save()
        print "The Example Calendar is created."
        print "Do we need to install the most common rules?"
        try:
            rule = Rule.objects.get(name="Daily")
        except Rule.DoesNotExist:
            print "Need to install the basic rules"
            rule = Rule(frequency = "YEARLY", name = "Yearly", description = "will recur once every Year")
            rule.save()
            print "YEARLY recurrence created"
            rule = Rule(frequency = "MONTHLY", name = "Monthly", description = "will recur once every Month")
            rule.save()
            print "Monthly recurrence created"
            rule = Rule(frequency = "WEEKLY", name = "Weekly", description = "will recur once every Week")
            rule.save()
            print "Weekly recurrence created"
            rule = Rule(frequency = "DAILY", name = "Daily", description = "will recur once every Day")
            rule.save()
            print "Daily recurrence created"
        print "Rules installed."
        '''
        print "Create some events"
        rule = Rule.objects.get(frequency="WEEKLY")
        data = {
                'title': 'Exercise',
                'start': datetime.datetime(2008, 11, 3, 8, 0),
                'end': datetime.datetime(2008, 11, 3, 9, 0),
                'end_recurring_period' : datetime.datetime(2009, 6, 1, 0, 0),
                'rule': rule,
                'calendar': cal
               }
        event = Event(**data)
        event.save()
        '''
