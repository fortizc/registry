import requests as req


class RestAPI:
    def __init__(self, host, port, user, passwd):
        self.__methods = {
            "V2_CHECK": "https://{host}:{port}/v2",
            "AVAILABLE_CATALOG": "https://{host}:{port}/v2/_catalog",
            "AVAILABLE_TAGS": "https://{host}:{port}/v2/{image}/tags/list"
        }

        self.__host = host
        self.__port = port
        self.__auth = (user, passwd)

        if not self.__is_v2_api():
            msg = "The API version 2 is not available on this host"
            raise RuntimeError(msg)

    def __is_v2_api(self):
        url = self.__methods["V2_CHECK"].format(host=self.__host,
                                                port=self.__port)
        code = req.get(url, auth=self.__auth).status_code
        return True if code == 200 else False

    def get_catalog(self):
        url = self.__methods["AVAILABLE_CATALOG"].format(host=self.__host,
                                                         port=self.__port)
        return req.get(url, auth=self.__auth).json()

    def get_tags(self, image):
        url = self.__methods["AVAILABLE_TAGS"]
        url = url.format(host=self.__host, port=self.__port, image=image)
        return req.get(url, auth=self.__auth).json()
