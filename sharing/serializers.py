from rest_framework import serializers

from sharing.models import *


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class VehicleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    brand = ProducerSerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = Vehicle
        fields = "__all__"


class BikeSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    brand = ProducerSerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = Bike
        fields = "__all__"


class DriveSerializer(serializers.ModelSerializer):
    driver = UserSerializer()
    vehicle = VehicleSerializer()
    bike = BikeSerializer()

    class Meta:
        model = Drive
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
