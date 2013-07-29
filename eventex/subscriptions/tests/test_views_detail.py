# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models  import Subscription


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(
            name='Bruno Nascimento', cpf='12345678901',
            email='brunolnascimento@gmail.com', phone='41-99305512')
        self.resp = self.client.get('/inscricao/%d/' % s.pk)

    def test_get(self):
        'Get /inscricao/1/ should return status 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses template'
        self.assertTemplateUsed(self.resp,
                         'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context must have a subscription instance'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was rendered.'
        self.assertContains(self.resp, 'Bruno Nascimento')