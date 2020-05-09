from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet

"""
Todo Study

Serializer는 다른 언어 or 서비스(ex 프론트)와 데이터를 주고 받을 때의 
데이터 인터페이스 제공을 위해 필요(json 등)
 

SnippetSerializer 인스턴스의 save()가 호출 될 때 create or update 함수가 호출
==> 어떤 기준으로 create 와 update가 호출 되지?
"""

"""
    ModelSerializer를 이용한 Serializer 선언
    create, update 메소드가 디폴트로 구현되어 있음
"""
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


"""
    Serializer를 이용한 Serializer 선언
"""
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")
#
#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
