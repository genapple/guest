# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guest.settings")
django.setup()
from django.test import  TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import  User
class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=2, name="oneplus 4 event  ", status=True, limit=2000, address='shenzhen',
                             start_time='2019-08-31 02:18:22')
        Guest.objects.create(id=2,event_id=1,realname='alen',
                             phone='136474839',email='alen@mail.com',sign=False)
    def test_event_models(self):
        result=Event.objects.get(name="oneplus 4 event")
        self.assertEqual(result.address,"shenzhen")
        self.assertTrue(result.status)
    def test_guest_models(self):
        result=Guest.objects.get('phone=136474839')
        self.assertEqual(result.realname,'alen')
        self.assertFalse(result.sign)

class IndexPageTest(TestCase):
    '''测试index登陆首页'''
    def test_index_page_renders_index_templeate(self):
        '''测试index视图'''
        response=self.client.get('/index/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')
class LoginActionTest(TestCase):
    '''测试登陆工作'''
    def setUp(self):
        user=User.objects.get(username="admin")
        self.assertEqual(user.username,"admin")
        self.assertEqual(user.email,"admin@mail.com")
    def test_login_action_username_password_null(self):
        '''用户名密码为空'''
        test_data={'username':'','password':''}
        response=self.Client.post("/login_action/",data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b'username or password error!',response.content)