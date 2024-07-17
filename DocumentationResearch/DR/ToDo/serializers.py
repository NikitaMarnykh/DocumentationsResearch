from rest_framework import serializers

from ToDo.models import TaskList


# Сериализатор списка задач
class TaskListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = TaskList
        fields = '__all__'
