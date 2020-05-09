from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

"""
Todo Study - Migrate

python manage.py makemigrations ${앱 이름}
==> 마이그레이션 파일 생성

python manage.py migrate
==> 마이그레이션 파일을 DB에 적용

마이그레이션 파일은 모델 클래스의 대한 변경을 추적, 실제로 DB에 적용
될 때는 SQL문이 날라감. 

python manage.py sqlmigrate ${앱이름} ${마이그레이션 파일 넘버}
==> 마이그레이션 적용 때 날라가는 쿼리 확인 
"""

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']
