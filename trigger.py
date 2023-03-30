import win32evtlog
import win32evtlogutil

class trigger:
    def trigger(self):
        DUMMY_DUMMY_APP_NAME = "DogodekA"
        DUMMY_EVENT_ID = 44
        DUMMY_EVENT_CATEG = 42
        DUMMY_EVENT_STRS = ["Dummy event string {0:d}".format(item) for item in range(5)]
        DUMMY_EVENT_DATA = b"Dummy event_data"

        win32evtlogutil.ReportEvent(DUMMY_DUMMY_APP_NAME, DUMMY_EVENT_ID, eventCategory=DUMMY_EVENT_CATEG, eventType=win32evtlog.EVENTLOG_ERROR_TYPE, strings=DUMMY_EVENT_STRS, data=DUMMY_EVENT_DATA)


    def logError(self, DUMMY_EVENT_ID, DUMMY_EVENT_STR):
        self.logSomething(DUMMY_EVENT_ID, DUMMY_EVENT_STR, win32evtlog.EVENTLOG_ERROR_TYPE)

    def logInfo(self, DUMMY_EVENT_ID, DUMMY_EVENT_STR):
        self.logSomething(DUMMY_EVENT_ID, DUMMY_EVENT_STR, win32evtlog.EVENTLOG_INFORMATION_TYPE)

    def logSomething(self, DUMMY_EVENT_ID, DUMMY_EVENT_STR, DUMMY_EVENT_TYPE):
        DUMMY_DUMMY_APP_NAME = "EventReader"
        DUMMY_EVENT_CATEG = 42
        DUMMY_EVENT_STRS = [DUMMY_EVENT_STR]
        DUMMY_EVENT_DATA = b"Dummy event_data"

        win32evtlogutil.ReportEvent(DUMMY_DUMMY_APP_NAME, DUMMY_EVENT_ID, eventCategory=DUMMY_EVENT_CATEG, eventType=DUMMY_EVENT_TYPE,
                                    strings=DUMMY_EVENT_STRS.append(DUMMY_EVENT_DATA.decode("utf-8")), data=DUMMY_EVENT_DATA)



t = trigger()
t.trigger()
#t.logInEvtLog(88, "Dodatno besedilo, za katerega bi rad, da se prikaže.")