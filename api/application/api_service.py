import datetime
from decimal import Decimal
import json
from sqlite3 import DatabaseError
from typing import Dict
from django.http import HttpRequest

class ApiService:

    def __init__(self, database):
        self.database = database

    def get_images(self, request: HttpRequest) -> Dict:
        with self.database.cursor() as cursor:
            cursor.execute("SELECT * FROM images")
            if cursor.fetchall():
                cursor.execute("SELECT id, name, weight, url, categories FROM images LEFT OUTER JOIN events ON images.id = events.image_id AND events.user_id = %s", [request.user.id])
                list_of_images = self.dictfetchall(cursor)
                for dicto in list_of_images:
                    cursor.execute("SELECT view, click FROM events RIGHT OUTER JOIN images ON events.image_id = %s AND events.user_id = %s", (dicto["id"], request.user.id))
                    dicto.update({'events': self.dictfetchone(cursor)})
                sorted_list = sorted(list_of_images, key=lambda i: i['weight'] if i['weight'] is not None else Decimal(0.0) , reverse=True)
                return { 'data' : sorted_list}
            else:
                raise DatabaseError("There are no images in the DB")

    def set_events(self, request: HttpRequest, imageId: str) -> None:
        body = json.loads(request.body.decode('utf-8'))
        with self.database.cursor() as cursor:
            # check the existence of the image
            cursor.execute("SELECT id FROM images WHERE id = %s", [imageId])
            if cursor.fetchall():
                #check if therte are events registered
                cursor.execute("SELECT * FROM events WHERE image_id = %s AND user_id = %s", (imageId, request.user.id))
                if cursor.fetchone() and body:
                    #select the eent to update
                    cursor.execute("SELECT * FROM events WHERE image_id = %s AND user_id = %s", (imageId, request.user.id))
                    data = self.dictfetchone(cursor)
                    data[body['eventType']] = data[body['eventType']] + 1
                    weight = self.weight_calculator(data)
                    cursor.execute("UPDATE events SET " + body['eventType'] + "= %s, weight = %s, updated_at = %s WHERE image_id = %s AND user_id = %s", (data[body['eventType']], weight, datetime.datetime.fromtimestamp(body['timestamp']), imageId, request.user.id))
                elif body:
                    #if there are no event registered insert a new record.
                    if body['eventType'].lower() == 'click':
                        cursor.execute("INSERT INTO events (user_id, image_id, view, click, weight, updated_at) VALUES (%s, %s, %s, %s, %s, %s)", ( request.user.id, imageId, 0, 1, 0.7, datetime.datetime.fromtimestamp(body['timestamp'])))
                    elif body['eventType'].lower() == 'view':
                        cursor.execute("INSERT INTO events (user_id, image_id, view, click, weight, updated_at) VALUES (%s, %s, %s, %s, %s, %s)", ( request.user.id, imageId, 1, 0, 0.3, datetime.datetime.fromtimestamp(body['timestamp'])))
                else:
                    raise DatabaseError("There are no event to record")
            else:
                raise DatabaseError("There are no image with the specified ID")
        return {}

    @classmethod
    def dictfetchall(cls, cursor):
        #Return all rows from a cursor as a dict
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    @classmethod
    def dictfetchone(cls, cursor):
        #Return one row from a cursor as a dict
        columns = [col[0] for col in cursor.description]
        return dict(zip(columns, cursor.fetchone()))

    @classmethod
    def weight_calculator(cls, data):
        weight = data['click'] * 0.7 + data['view'] * 0.3
        return weight
