class Urls:
    @staticmethod
    def main_url():
        return "https://2gis.ru/Moscow"

    @staticmethod
    def pc_version():
        return ("https://info.2gis.ru/moscow/products/download?utm_"
                "source=online&utm_medium=product&utm_campaign=sidebar")

    @staticmethod
    def android_version():
        return ("https://play.google.com/store/apps/details?id=ru."
                "dublgis.dgismobile&af_ss_ver=2_7_2&af_ss_ui=true&c=sideMenu&pid="
                "online&deep_link_value=dgis%3A%2F%2F2gis.ru%2F&af_sub4=online&af_js_web=true&af_sub5=sideMenu")

    @staticmethod
    def ios_version():
        return ("https://apps.apple.com/ru/app/2%D0%B3%D0%B8%D1%81-"
                "%D0%BA%D0%B0%D1%80%D1%82%D1%8B-%D0%BD%D0%B0%D0%B2%D0%B8%D0"
                "%B3%D0%B0%D1%82%D0%BE%D1%80-%D0%B4%D1%80%D1%83%D0%B7%D1%8C%D1%8F/id481627348?mt=8")


class User:
    @staticmethod
    def user_data():
        return {
            "email": "example.qa.auto@gmail.com",
            "password": "1qwert24"
        }
