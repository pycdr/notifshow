#!/usr/bin/env python3
from argparse import ArgumentParser
import notify2

parser = ArgumentParser(
	description = "notifshow is used to show a notification as simple as possible.",
	prog = "notifshow",
	epilog = "waiting for you at https://github.com/pycdr/notifshow"
)

parser.add_argument(
	"title",
	help = "title of the notification",
	type = str
)
parser.add_argument(
	"text",
	help = "description of the notification",
	type = str,
	default = ""
)

args = parser.parse_args()

notify2.init(args.title)
notif = notify2.Notification(args.title)

notif.update(args.title, args.text)
notif.show()
