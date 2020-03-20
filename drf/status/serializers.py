
from rest_framework import serializers
from .models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'user', 'content', 'image']
        read_only_fields = ['user']

    def validate_content(self,value):
        if len(value)>10000:
            raise serializers.ValidationError("this one is big for real")
        return value

    def validate_image(self,value):
        pass

    # def validate(self, data):
    #     content = data.get["content"]
    #     image = data.get["image", None]
    #     if content == "":
    #         content = None
    #     if content is None and image is None:
    #         raise serializers.ValidationError("Fuck This Shit Am out")
    #     return data