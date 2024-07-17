from rest_framework import serializers
from .models import Quote

# Сериализация моделей для API


# Сериализатор котировок
class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'
