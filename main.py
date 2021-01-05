#!/usr/bin/env python3
from argparse import ArgumentParser
from tools.icon import icon_path
from tools.urg import URG_NUMBER
import notify2

parser = ArgumentParser(
	description = "notifshow is used to show a notification as simple as possible.",
	prog = "notifshow",
	epilog = "waiting for you at https://github.com/pycdr/notifshow"
)

parser.add_argument(
	"title",
	help = "title of the notification.",
	type = str
)
parser.add_argument(
	"text",
	help = "description of the notification.",
	type = str,
	default = ""
)
parser.add_argument(
	"-i", "--icon",
	help = "icon of the notification. it may be a path or one of these words: info ,error, stop.",
	type = str,
	required = False,
	default = ""
)
parser.add_argument(
	"-n", "--name",
	help = "name of the notification(s).",
	type = str,
	default = "notifshow"
)
parser.add_argument(
	"-t", "--timeout",
	help = "set the time how long the notification is shown (as milisecond).",
	type = int,
	default = 5000
)
parser.add_argument(
	"-u", "--urgency",
	help = "the level of the urgency",
	choices = ["low", "normal", "critical"],
	required = False,
	default = "normal"
)

args = parser.parse_args()

notify2.init(args.name)
notif = notify2.Notification(None, icon = args.icon)

notif.set_timeout(args.timeout)
notif.set_urgency(URG_NUMBER[args.urgency])

notif.update(args.title, args.text)
notif.show()
