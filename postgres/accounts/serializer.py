from rest_framework import serializers

from .models import Accounts

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'email'
        ]




# JSON Query for writing user details in custom accounts db

"""{
"first_name": "abdul",
"last_name": "ghani",
"username": "aghani",
"password": "1234", 
"email":"agaarbi@gmail.com"
}"""