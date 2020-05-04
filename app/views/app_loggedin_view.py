# -*- coding:utf-8 -*-

from app.views.app_base_view import *
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Option

'''
　アプリ内共通処理
'''
class AppLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'
    _option = None

    def getOption(self):
        if self._option == None:
            self._option = Option.objects.get(pk=1)
        return self._option

class AppLoggedinListView(AppLoginRequiredMixin, AppBaseListView):
    ''' just override '''

class AppLoggedinDetailView(AppLoginRequiredMixin, AppBaseDetailView):
    ''' just override '''

class AppLoggedinCreateView(AppLoginRequiredMixin, AppBaseCreateView):
    ''' just override '''

class AppLoggedinUpdateView(AppLoginRequiredMixin, AppBaseUpdateView):
    ''' just override '''

class AppLoggedinDeleteView(AppLoginRequiredMixin, AppBaseDeleteView):
    ''' just override '''

class AppLoggedinTemplateView(AppLoginRequiredMixin, AppBaseTemplateView):
    ''' just override '''
