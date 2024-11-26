from typing import Union
import csv
import json
import logging

from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.responses import FileResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CordubaRESTAPI")

# Create server instance
app = FastAPI()


# from demo, can be removed
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# from demo, can be removed
@app.get("/")
def read_root():
    return 'Corduba server version'
    # return { "Hello": "World"}


# from demo, can be removed
@app.get("/items/{item_id}")
def read_item(item_id : int, q: Union[str, None] = None):
    return { "item_id": item_id, "q": q}


# from demo, can be removed
@app.put("/items/{item_id}")
def update_item(item_id : int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# user 0 : demonstrator, user 1: real
@app.get("/provision_day/{user}/")
async def get_day_provisioning(user : int):

    logger.info("Accessing daily provisioning for user " + str(user))
    csv_data = []
    provisioning_filename = "data/user_" + str(user) + ".csv"
    logger.info("Reading from " + provisioning_filename)
    with open(provisioning_filename, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            logger.info("Entry found in csv " + str(row))
            csv_data.append(dict(zip(header, row)))

    json_data = json.dumps(csv_data)

    return json.loads(json_data)


# get the current model
@app.get("/current_model")
def get_current_model():
    file_path = "data/current_model/model.ptl"
    logger.info("Fetching model from " + file_path)
    return FileResponse(file_path,
                        media_type='application/octet-stream',
                        filename='model.ptl',
                        headers={"ContentDisposition":"attachment; filename=model.ptl"})
