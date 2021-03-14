from flask_restful import Api
from controller.pasteController import PasteAPI, PasteOtherAPI

def api_routes(api: Api):
    api.add_resource(PasteAPI, '/')
    api.add_resource(PasteOtherAPI, '/<shortCode>/')

    return api