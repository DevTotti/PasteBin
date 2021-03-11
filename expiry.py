from models.pasteModel import Paste, DeleteExpired
from mongoengine import connect
from dotenv import load_dotenv
import os, json
from datetime import datetime
from dateutil.parser import parse


load_dotenv()
connect(host= os.environ["HOST"])

def deleteDocument():
    print("starting operation")

    paste_db, expiry_db = Paste, DeleteExpired

    exp_data = expiry_db.objects()

    exp_data = exp_data.to_json()

    exp_data_ = eval(exp_data)

    for doc_data in exp_data_:
        print(doc_data)
        date = doc_data['date']
        expiry = doc_data['expiry']
        obj_id = doc_data['obj_id']

        date = parse(date)
        present_date = datetime.now()

        date_diff = present_date - date
        date_diff_ = date_diff.total_seconds()

        if date_diff_ >= expiry:
            delete_expired_paste_ = paste_db.objects(id=obj_id).delete()
            delete_expired_expiry = expiry_db.objects(obj_id=obj_id).delete()
            if delete_expired_paste_ and delete_expired_expiry:
                response = {'result': 'paste bin data deleted'}
                print(response)

        

    # print(exp_data)
