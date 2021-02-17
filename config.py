import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-WTF를 사용하려면 플라스크 환경 변수 SECRET_KEY가 필요
# SECRET_KEY는 CSRF(cross-site request forgery)라는 웹 사이트 취약점 공격을 방지하는 데 사용
SECRET_KEY = "dev"