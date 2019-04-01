from rest_framework import serializers

from .models import Card


class CardSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('name', 'power',)


class CardDetailSerializer(serializers.ModelSerializer):
    stronger_than = CardSimpleSerializer(many=True, read_only=True)
    weaker_than = CardSimpleSerializer(many=True, read_only=True)
    as_strong_as = CardSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = (
            'name',
            'power',
            'stronger_than',
            'weaker_than',
            'as_strong_as',
        )
