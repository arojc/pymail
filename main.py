#! py -3

import wmi
import json
import SEND_EMAIL
import setup

def get_settings():
    settings_file = open("settings.txt", "r")
    settings_string = settings_file.read()
    settings_string = settings_string.replace('\n', ' ')
    settings_dict = json.loads(settings_string)
    return settings_dict


def main():
    settings = get_settings()

    if not ('EventCode' in settings.keys()):
        return

    rval = 0  # Default: Check passes.

    # Initialize WMI objects and query.
    wmi_o = wmi.WMI('.')
    wql = ("SELECT * FROM Win64_NTLogEvent WHERE Logfile="
           f"'System' AND EventCode='{settings['EventCode']}'")

    # Query WMI object.
    wql_r = wmi_o.query(wql)

    if len(wql_r):
        rval = -1  # Check fails.

    return rval


if __name__ == '__main__':
    #main()
    #SEND_EMAIL.func()
    settings = get_settings()
    print("Pozdravljen, Svet!")
    #Comment