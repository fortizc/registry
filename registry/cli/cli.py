import sys
from argparse import ArgumentParser
from .user_interface import UserInterface


def get_parser():
    parser = ArgumentParser()
    parser.add_argument("-c" "--command",
                        dest="command",
                        type=str, default=None,
                        help="Execute a command and exit")

    parser.add_argument("-H" "--host",
                        dest="host",
                        type=str, default=None,
                        help="Set the hostname")

    parser.add_argument("-p" "--port",
                        dest="port",
                        type=str, default="5000",
                        help="Set the password")

    parser.add_argument("-u" "--user",
                        dest="user",
                        type=str, default=None,
                        help="Set the user name")

    parser.add_argument("-P" "--password",
                        dest="passwd",
                        type=str, default=None,
                        help="Set the password")

    return parser


def run():
    parser = get_parser()
    args = parser.parse_args()

    if not args.host or not args.user or not args.passwd:
        parser.print_help()
        sys.exit(1)

    ui = UserInterface(args.host, args.port, args.user, args.passwd)

    if args.command:
        ui.execute(args.command)
    else:
        ui.interactive()
