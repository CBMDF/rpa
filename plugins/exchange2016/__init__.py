from plugins.browser import Browser


class exchange2016(Browser):

    def __init__(self):
        super().__init__()

    def login(self, url, username, password):
        super().openUrl(url)
        super().fill('//*[@id="username"]', username)
        super().fill('//*[@id="password"]', password)
        super().click('/html/body/form/div/div[2]/div/div[9]/div')

    def search_message()
