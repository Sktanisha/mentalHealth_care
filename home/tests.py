from django.test import TestCase
from home.models import accounts, msgs, quizresult, psychiatrist

# Create your tests here.
class TestClass(TestCase):
    def testAccount(self):
        self.accounts = accounts.objects.create (
            name='Mita',
            age= 12,
            address= 'abcd',
            mobile= 1234,
            email= 'mita@gmail.com',
            )
        self.assertEquals(self.accounts.name,'Mita')
        self.assertEquals(self.accounts.age,12)
        self.assertEquals(self.accounts.address,'abcd')
        self.assertEquals(self.accounts.mobile,1234)
        self.assertEquals(self.accounts.email,'mita@gmail.com')

    def testMsg(self):
        self.msgs = msgs.objects.create (
            person_name='Mita',
            msg= 'abcd',
            person_contact= 1234,
            person_email= 'mita@gmail.com',
            )
        self.assertEquals(self.msgs.person_name,'Mita')
        self.assertEquals(self.msgs.msg,'abcd')
        self.assertEquals(self.msgs.person_contact,1234)
        self.assertEquals(self.msgs.person_email,'mita@gmail.com')

    def testResult(self):
        self.quizresult = quizresult.objects.create (
            name='david',
            result = 'anxiety'
            )
        self.assertEquals(self.quizresult.name,'david')
        self.assertEquals(self.quizresult.result,'anxiety')

    def testDoctor(self):
        self.psychiatrist = psychiatrist.objects.create (
            name='david',
            designation = 'CADC',
            ps_email = 'david@gmail.com',
            ps_mobile = 1234, 
            )
        self.assertEquals(self.psychiatrist.name,'david')
        self.assertEquals(self.psychiatrist.designation,'CADC')
        self.assertEquals(self.psychiatrist.ps_email,'david@gmail.com')
        self.assertEquals(self.psychiatrist.ps_mobile,1234)

    def test_index_url_name(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_authenticate_url_name(self):
        response = self.client.get('/authenticate')
        self.assertEqual(response.status_code, 404)
    
    def test_login_url_name(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
    
    def test_register_url_name(self):
        response = self.client.get('/register')
        self.assertEquals(response.status_code, 200)

    def test_contact_form_url_name(self):
        response = self.client.get('/contact_form')
        self.assertEquals(response.status_code, 200)

    def test_edit_profile_url_name(self):
        response = self.client.get('/edit_profile')
        self.assertEquals(response.status_code, 302)

    def test_quizform_url_name(self):
        response = self.client.get('/quizform')
        self.assertEquals(response.status_code, 200)

    def test_result_url_name(self):
        response = self.client.get('/result')
        self.assertEquals(response.status_code, 200)

    def test_psychiatrist_url_name(self):
        response = self.client.get('/psychiatrist')
        self.assertEquals(response.status_code, 404)

    



    # @classmethod
    
    # def setUpTestData(cls):
    #     accounts.objects.create(name='test', email='test@gmail.com')
    #     msgs.objects.create(person_name='Rachel',person_email='rachel@gmail.com')

    # def test_user_name(self):
    #     user = accounts.objects.get(id=6)
    #     field_label = user._meta.get_field('name').verbose_name
    #     # print("Method: testing name field")
    #     self.assertEqual(field_label, 'name', "Testing name in user")

    # def test_userobject_name_email(self):
    #     user = accounts.objects.create(name='Bob', email='bob@gmail.com')
    #     object_name = f'{user.name}'
    #     object_email = f'{user.email}'
    #     # print("Method: Checking/Matching name and email")
    #     self.assertEqual('Bob', object_name, "Testing Name")
    #     self.assertEqual('bob@gmail.com', object_email, "Testing Email")

    def testAdd(self):
        result = 10+5
        self.assertEquals(result,15)