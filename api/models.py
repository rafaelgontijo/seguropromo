from api import Api


class Benefits(Api):
    """ Object from benefits """

    def list(self):
        url = "{}/additional-info/benefits".format(self.base_url)
        return super(Benefits, self).get(url)


class Destinations(Api):
    """ Object from destinations """

    def list(self):
        url = "{}/additional-info/destinations".format(self.base_url)
        return super(Destinations, self).get(url)


class Providers(Api):
    """ Object from providers """

    def list(self):
        url = "{}/additional-info/providers".format(self.base_url)
        return super(Providers, self).get(url)


class PaymentMethod(Api):
    """ Object from payment method """

    def list(self):
        url = "{}/paymentmethod".format(self.base_url)
        return super(PaymentMethod, self).get(url)


class Products(Api):
    """ Object from products """

    def list(self, code):
        url = "{}/products/{}".format(self.base_url, code)
        return super(Products, self).get(url)


class Quotation(Api):
    """ Object from quotation """

    def calculate(self, **kwargs):
        url = "{}/quotations".format(self.base_url)
        body = {
            "begin_date": "{:%Y-%m-%d}".format(kwargs.get('begin_date')),
            "end_date": "{:%Y-%m-%d}".format(kwargs.get('begin_date')),
            "destination": kwargs.get('destination'),
        }
        return super(Quotation, self).post(url, body)


class Purchase(Api):
    """ Object from purchase """

    def buy(self,  **kwargs):
        url = "{}/purchases-redirect".format(self.base_url)
        body = {
            "product_code": kwargs.get('product_code'),
            "destination": kwargs.get('destination'),
            "coverage_begin": "{:%Y-%m-%d}".format(kwargs.get('begin_date')),
            "coverage_end": "{:%Y-%m-%d}".format(kwargs.get('end_date'))
        }
        return super(Purchase, self).post(url, body)
