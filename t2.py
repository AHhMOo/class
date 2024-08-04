class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0 

    def add_participant(self):
        """Increase the participant count by 1."""
        self.participant_count += 1

    def get_participant_count(self):
        """Return the current participant count."""
        return self.participant_count

my_event = Event("Tech Conference", "2024-08-04")

my_event.add_participant()
my_event.add_participant()

print("Current participant count:", my_event.get_participant_count())

my_event.add_participant() #this is for add if you want >3
print("Updated participant count:", my_event.get_participant_count())
