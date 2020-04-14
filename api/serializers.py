from rest_framework import serializers

from api.estimator import Estimator, LANGUAGES_CHOICES


class EstimatorSerializer(serializers.Serializer):
    period_type = serializers.ChoiceField(choices=LANGUAGES_CHOICES, default='days')
    time_to_elapse = serializers.IntegerField()
    reported_cases = serializers.IntegerField()
    population = serializers.IntegerField()
    total_hospital_beds = serializers.IntegerField()

    def create(self, validated_data):
        return Estimator(**validated_data)

    def update(self, instance, validated_data):
        instance.period_type = validated_data.get('period_type', instance.period_type)
        instance.time_to_elapse = validated_data.get('time_to_elapse', instance.time_to_elapse)
        instance.reported_cases = validated_data.get('reported_cases', instance.reported_cases)
        instance.population = validated_data.get('population', instance.population)
        instance.total_hospital_beds = validated_data.get('totalHospitalBeds', instance.total_hospital_beds)
        return instance
