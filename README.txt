!Пишу по памяти, скорее всего мог что-то забыть!
Если есть ошибки, лучше пришлите мне их скрин в вк vk.com/arslan.gareev или на почту, скорее всего я с ней уже встречался и вам не придется тратить время на поиск её решения.


Подключение необходимых пакетов (то,что помню)

pip install django
pip install twisted 
pip install channels 
pip install asyncio
____________________________________________________________________________________________


Создание триггера в postgreSQL

#создание таблицы
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  total BIGINT NOT NULL
);

#создание триггерной функции, которую мы будем подключать к самому триггеру
#функция сразу выдает результат в JSON
CREATE OR REPLACE FUNCTION notify_event() RETURNS TRIGGER AS $$
  DECLARE
    record RECORD;
    payload JSON;
  BEGIN
    IF (TG_OP = 'DELETE') THEN
      record = OLD;
    ELSE
      record = NEW;
    END IF;

    payload = json_build_object('table', TG_TABLE_NAME,
                                'action', TG_OP,
                                'data', row_to_json(record));

    PERFORM pg_notify('events', payload::text);

    RETURN NULL;
  END;
$$ LANGUAGE plpgsql;

#создание непосредственно триггера для нашей таблицы, созданной ранее
CREATE TRIGGER notify_order_event
AFTER INSERT OR UPDATE OR DELETE ON orders
  FOR EACH ROW EXECUTE PROCEDURE notify_event();

____________________________________________________________________________________________

Подключение posgtreSQL в django

В файле settings.py, который находится в корневой папке проекта необходимо найти строчку DATABASES и поменять параметры в соответствии с вашими.

Также и в файле consumers.py, находящийся в папке scada\control

____________________________________________________________________________________________

Теперь при добавлении данных в нашу таблицу, функция get_data_opc, описанная в файле consumers.py будет отсылать на фронтенд добавленные данные. Посмотреть отсылаемые данные на страницу можно следующим образом : Google Chrome: исследовать элемент -> во вкладке console будут выводиться логи.

Я добавляю данные таким образом (если добавить через psql, он почему-то не захочет прослушивать (LISTEN) данные):
import psycopg2

con = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='Direling2017'")
cur = con.cursor()

cur.execute(f"INSERT into orders (total) VALUES (7);")

con.commit()

con.close()

____________________________________________________________________________________________

Как поиграться с графиком, который пока работает только по http:

В папке scada\control есть файл views.py, который как раз таки и отвечает за передачу данных, да и в целом рендер страницы и др. по http запросу. В этом файле есть функция chart, которая обращается к некоторой таблице. Если заполнить таблицу данными, то при перезагрузке страница, выведется график.



P.S. Наверное у вас будет куча ошибок и вопросов, так что пишите мне в любое время, я постараюсь объяснить. Просто в тексте сложно объяснить всё сразу.
















