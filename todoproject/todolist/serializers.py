from rest_framework import serializers
from .models import Task, Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    # status_id = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    status_id = StatusSerializer()

    # status_id = serializers.ChoiceField(['1', '2', '3', '4'])
    # status_id = serializers.ChoiceField(choices=Status.objects.values_list('id', flat=True))

    class Meta:
        model = Task
        fields = ('id', 'name', 'desc', 'create_time', 'update_time', 'status_id')

    def create(self, validated_data):
        status_data = validated_data.pop('status_id')
        status = Status.objects.get(name_status='open')
        task = Task.objects.create(status_id=status, **validated_data)
        return task
