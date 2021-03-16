#### Саме собою не запуститься
##### Наступні налаштування

postgresql+psycopg2://юзер:пароль@localhost/база_даних

Встановити змінні середовища

```
set APP_SETTINGS=config.DevelopmentConfig
set DATABASE_URL=postgresql+psycopg2://postgres:mySecretPost@localhost/wordcount_dev
```
``DATABASE_URL`` використовується в ```models.py``` як ```os.environ['DATABASE_URL']```

В рекваєрментах є багато лишніх ліб але на це все-одно

Далі

```alembic init alembic```
Появилася папка алембік, поки без міграцій

![img_1.png](img_1.png)

Той сам щлях треба прописати в ```alembic.ini```(змінна ```sqlalchemy.url```) Тут через os вже не вийде

У файлі ```env.py``` у змінній ```target_metadata``` треба присвоїти значення ```Base.metadata```
Для цього імпротнем ````Base```` з ```models.py``` - 

```from models import Base```

Далі

----
env.py
```angular2html
target_metadata = Base.metadata
```

Тепер створимо міграцію на табличку Резалтc з моделей, яка створиться оскільки в ``app.py`` імпортовано клас Results

```alembic revision --autogenerate -m "Nazwa migraciji"```

Тепер у папці ```versions``` створилася перша міграція 

![img_7.png](img_7.png)

В міграції видно які колонки створюються

![img_3.png](img_3.png)

Застосуємо міграції

```alembic upgrade head```

(head - це остання, можна і якусь конкретну)

Тепер в бд є табличка резалтс і дефолтна алембіку

![img_8.png](img_8.png)

Якби у нас була б одразу папка алембік, а в ній міграції, то для того щоб створити собі таблички вистачило 
б просто команди

```alembic upgrade head```

усьо

![alt text](ezgif-6-149cfa588071.gif)
