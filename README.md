# 比赛评分

## 环境初始化
```bash
python3 -m pip install --upgrade pip
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install setuptools
pip3 install pipenv

pipenv install
pipenv shell

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```