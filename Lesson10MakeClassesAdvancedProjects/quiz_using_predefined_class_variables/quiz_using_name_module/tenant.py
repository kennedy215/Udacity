import webbrowser

class Apartment():
    """For the print __name__ and __module assignment I created a template for an apartment decided to add
dating interview videos since their aren't any apartment interview videos. Enjoy!"""
    ROOMS = ["1","2","3","4"]
    def __init__(self,apartment_rates,apartment_tenant,apartment_lease,apartment_interview):
        self.rates = apartment_rates
        self.tenant = apartment_tenant
        self.lease = apartment_lease
        self.interview = apartment_interview


    def show_commercial(self):
        webbrowser.open(self.interview)
