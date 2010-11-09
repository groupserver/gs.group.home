# coding=utf-8
from admin import AdminTab

class AboutTab(AdminTab):
    @property
    def aboutText(self):
        return getattr(self.context, 'aboutText', '')

