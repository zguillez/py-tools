import os
from python_toolz import helper as ztools


ztools.log("test")

db = ztools.database({
    'conn': os.environ['DB_HOST'],
    'database': os.environ['DB_NAME'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASS']
})
data = db.dict("SELECT id, name FROM template ORDER BY id ASC LIMIT 0,5", ['id', 'name'])
db.close()
print(data[0]['name'])

ztools.log("done!")
