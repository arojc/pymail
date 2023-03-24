import win32evtlog
import win32evtlogutil

class trigger:
    def trigger(self):
        DUMMY_DUMMY_APP_NAME = "Ime"
        DUMMY_EVENT_ID = 66
        DUMMY_EVENT_CATEG = 42
        DUMMY_EVENT_STRS = ["Dummy event string {0:d}".format(item) for item in range(5)]
        DUMMY_EVENT_DATA = b"Dummy event_data"

        win32evtlogutil.ReportEvent(DUMMY_DUMMY_APP_NAME, DUMMY_EVENT_ID, eventCategory=DUMMY_EVENT_CATEG, eventType=win32evtlog.EVENTLOG_ERROR_TYPE,
                                    strings=DUMMY_EVENT_STRS, data=DUMMY_EVENT_DATA)

    # def trigger(self, app, id, evCategory, evType):
    #     win32evtlogutil.ReportEvent(app, id, eventCategory=evCategory, eventType=evType)

t = trigger()
t.trigger()