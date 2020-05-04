# -*- coding:utf-8 -*-
#from django.contrib import messages

from django.views.generic import \
    View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

'''
　アプリ内共通処理
'''
class AppBaseSessionMixin:
    '''
    def set_default_site(self):
        site = Site.objects.order_by('id').first()
        self.request.session['site'] = { 'id': site.id, 'site_name': site.site_name }

    def active_site(self):
        if self.request.user.is_staff:
            if not 'site' in self.request.session:
                self.set_default_site()
            return self.request.session['site']
        else:
            return self.request.user.site

    def site_list(self):
        if self.request.user.is_staff:
            return Site.objects.order_by('id').all()
        else:
            return [self.request.user.site]

    '''
    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_authenticated:
            context['auth_user'] = self.request.user
            #context['active_site'] = self.active_site()
            #context['site_list'] = self.site_list()
            if self.request.user.is_staff:
                context['is_admin'] = True
            else:
                context['is_admin'] = False
            #if not 'menu_mode' in context:
            #    context['menu_mode'] = 'site'
        return super().render_to_response(context, **response_kwargs)

class AppBaseListView(AppBaseSessionMixin, ListView):
    ''' just override '''

class AppBaseDetailView(AppBaseSessionMixin, DetailView):
    ''' just override '''

class AppBaseCreateView(AppBaseSessionMixin, CreateView):
    ''' just override '''

class AppBaseUpdateView(AppBaseSessionMixin, UpdateView):
    ''' just override '''

class AppBaseDeleteView(AppBaseSessionMixin, DeleteView):
    ''' just override '''

class AppBaseTemplateView(AppBaseSessionMixin, TemplateView):
    ''' just override '''
