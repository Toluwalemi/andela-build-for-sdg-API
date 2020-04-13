from rest_framework import serializers
from api.estimator import estimator


class RegionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    avgAge = serializers.FloatField()
    avgDailyIncomeInUSD = serializers.DecimalField(max_digits=5, decimal_places=2)
    avgDailyIncomePopulation = serializers.FloatField()


class EstimatorSerializer(serializers.Serializer):
    region = RegionSerializer()
    periodType = serializers.CharField(max_length=10)
    timeToElapse = serializers.IntegerField()
    reportedCases = serializers.IntegerField()
    population = serializers.IntegerField()
    totalHospitalBeds = serializers.IntegerField()

    def create(self, validated_data):
        return estimator(**validated_data)

    # def update(self, instance, validated_data):
    #     for field, value in validated_data.items():
    #         setattr(instance, field, value)
    #     return instance
