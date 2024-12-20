from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from datetime import date



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
    

    def validate(self, attrs):

        if attrs['status'] == 'completed' and not attrs.get('completed_at'):
            raise serializers.ValidationError({
                'completed_at': 'This field is mandatory when status is completed.'
                })
        created_at_raw = self.initial_data.get('created_at')

        if attrs.get('completed_at') and created_at_raw:
            if attrs['completed_at'] < serializers.DateField().to_internal_value(created_at_raw):
                raise serializers.ValidationError({
                    'completed_at': 'This field is always greater than the created date.'
                    })
        
        if attrs.get('completed_at') and attrs['completed_at'] > date.today():
            raise serializers.ValidationError({
                'completed_at': 'This field must not be a future date.'
                })
        
        return super().validate(attrs)

