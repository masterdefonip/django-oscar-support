from django.conf.urls.defaults import patterns, url

from oscar.core.application import Application

from ticketing import views


class TicketingApplication(Application):
    name = 'ticketing'

    ticket_list_view = views.TicketListView
    ticket_create_view = views.TicketCreateView
    ticket_update_view = views.TicketUpdateView

    def get_urls(self):
        urlpatterns = super(TicketingApplication, self).get_urls()

        urlpatterns += patterns('',
            url(
                r'accounts/support/$',
                self.ticket_list_view.as_view(),
                name='customer-ticket-list'
            ),
            url(
                r'accounts/support/ticket/create/$',
                self.ticket_create_view.as_view(),
                name='customer-ticket-create'
            ),
            url(
                r'accounts/support/ticket/(?P<pk>\d+)/update/$',
                self.ticket_update_view.as_view(),
                name='customer-ticket-update'
            ),
        )
        return self.post_process_urls(urlpatterns)


application = TicketingApplication()
