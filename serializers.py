from rest_framework import serializers
from .models import housingsociety
from .models import blocks
from .models import apartment
from .models import citizens




class housingserializer(serializers.ModelSerializer):
    class Meta:
        model = housingsociety

        #fields=('firstname', 'lastname', 'emp_id')
        fields = '__all__'

class blockserializer(serializers.ModelSerializer):
    class Meta:
        model = blocks

        fields = '__all__'

class apartmentserializer(serializers.ModelSerializer):
    class Meta:
        model=apartment

        fields='__all__'

class citizensserializer(serializers.ModelSerializer):
    class Meta:
        model = citizens

        fields='__all__'

