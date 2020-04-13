from rest_framework import serializers
from api.estimator import estimator


class RegionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    avgAge = serializers.FloatField()
    avgDailyIncomeInUSD = serializers.CharField(max_length=5)
    avgDailyIncomePopulation = serializers.FloatField()


class EstimatorSerializer(serializers.Serializer):
    region = RegionSerializer(required=False)
    # avg_income = serializers.DecimalField(max_digits=5, decimal_places=2)
    # avg_income_population = serializers.FloatField()
    periodType = serializers.CharField(max_length=10)
    timeToElapse = serializers.IntegerField()
    reportedCases = serializers.IntegerField()
    population = serializers.IntegerField()
    totalHospitalBeds = serializers.IntegerField()

    def create(self, validated_data):
        return estimator(**validated_data)

    def update(self, instance, validated_data):
        instance.region = validated_data.get('region', instance.region)
        # instance.avg_income = validated_data.get(['region', 'name'], instance.avg_income)
        # instance.avg_income = validated_data.get(['region', 'avgDailyIncomeInUSD'], instance.avg_income)
        instance.periodType = validated_data.get(['periodType', 'avgDailyIncomePopulation'], instance.periodType)
        # instance.period_type = validated_data.get('periodType', instance.avg_income)
        instance.timeToElapse = validated_data.get('timeToElapse', instance.timeToElapse)
        instance.reportedCases = validated_data.get('reportedCases', instance.reportedCases)
        instance.totalHospitalBeds = validated_data.get('totalHospitalBeds', instance.totalHospitalBeds)
        instance.save()
        return instance
