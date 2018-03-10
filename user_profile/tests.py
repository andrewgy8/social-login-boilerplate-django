from django.test import TestCase
from .forms import SignUpForm


class SignUpFormTest(TestCase):

    def test_empty_data(self):
        form = SignUpForm({})
        assert 'username' in form.errors
        assert 'birth_date' in form.errors
        assert 'password1' in form.errors
        assert 'password2' in form.errors

    def test_too_short_password(self):
        form = SignUpForm({'username': 'Andrew',
                           'birth_date': '2001-06-04',
                           'password1': 'happy',
                           'password2': 'happy'})
        self.assertFalse(form.is_valid())
        assert form.errors

    def test_incorrect_date_format(self):
        form = SignUpForm({'username': 'Andrew',
                           'birth_date': '2001/06/04',
                           'password1': 'happy1234',
                           'password2': 'happy1234'})
        self.assertFalse(form.is_valid())
        assert form.errors

    def test_valid_data(self):
        form = SignUpForm({'username': 'Andrew',
                           'birth_date': '2001-06-04',
                           'password1': 'happy1234',
                           'password2': 'happy1234'})
        self.assertTrue(form.is_valid())
