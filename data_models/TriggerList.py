import json

class TriggerClass:
    def __init__(self):
        self.Records = []

class Trigger:
    def __init__(self):
        self.EventID = 0
        self.EventName = None
        self.Receiver = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
