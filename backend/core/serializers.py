from rest_framework import serializers
from .models import Todo, Category

from .functions import attempt_json_deserialize

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    category = CategorySerializer(readonly=True)
    class Meta:
        model = Todo
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context['request']
 
        category_pk = request.data.get('category')
        category_pk = attempt_json_deserialize(category_pk, expect_type=str)
        validated_data['category_id'] = category_pk
 
        instance = super().create(validated_data)
 
        return instance
    
    def update(self, instance, validated_data):
        request = self.context['request']
 
        category_data = request.data.get('category')
        category_data = attempt_json_deserialize(category_data, expect_type=str)
        validated_data['category_id'] = category_data
 
        instance = super().update(instance, validated_data)
 
        return instance

class ToDoSummarySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Todo
        fields = ('id', 'title')
 
 
class CategoryDetailSerializer(serializers.ModelSerializer):
    group = ToDoSummarySerializer(read_only=True, many=True)
 
    class Meta:
        model = Category
        fields = ('id', 'title', 'group')
        