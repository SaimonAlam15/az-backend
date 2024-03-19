from rest_framework.serializers import ModelSerializer

from .models import User, AddressBook


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name',
            'phone', 'is_active', 'role'
        ]


class AddressBookSerializer(ModelSerializer):
    class Meta:
        model = AddressBook
        fields = ['id', 'address', 'city', 'zip', 'label']
        extra_kwargs = {
            'user': {'write_only': True}
        }
        read_only_fields = ['id']