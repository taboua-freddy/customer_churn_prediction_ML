from rest_framework import serializers
from . models import churn

class churnsSerializers(serializers.ModelSerializer):
	class Meta:
		model=churn
		fields='__all__'