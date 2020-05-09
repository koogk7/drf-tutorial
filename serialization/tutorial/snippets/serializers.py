from django.contrib.auth.models import User
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
        owner = serializers.ReadOnlyField(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']