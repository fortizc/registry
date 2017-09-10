from ..lib.rest_api import RestAPI
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory


class UserInterface:
    def __init__(self, host, port, user, passwd):
        self.__api = RestAPI(host, port, user, passwd)
        self.__commands = {
            "images": self.__show_catalog,
            "tags": self.__show_tags
        }
        self.custom_prompt = "{user}@{host}: ".format(host=host, user=user)

    def __show_catalog(self):
        rsp = self.__api.get_catalog()
        for img in rsp["repositories"]:
            print("* " + img)

    def __show_tags(self, image):
        if not image:
            print ("Error, an image name is required")
            return
        rsp = self.__api.get_tags(image)
        if rsp.get("errors", None):
            print("Image not found!")
            return

        print("* " + rsp["name"] + ":")
        rsp["tags"].sort()
        for tag in rsp["tags"]:
            print("\t" + tag)

    def execute(self, command):
        if command == "exit":
            return

        cmd = command.split(" ")

        if not cmd or not self.__commands.get(cmd[0], None):
            print ("Command not found!")
            return

        if len(cmd) == 2:
            self.__commands[cmd[0]](cmd[1])
        elif len(cmd) == 1:
            self.__commands[cmd[0]]()

    def interactive(self):
        history = InMemoryHistory()
        cmd = ""
        while cmd != "exit":
            cmd = prompt(self.custom_prompt, history=history)
            self.execute(cmd)
