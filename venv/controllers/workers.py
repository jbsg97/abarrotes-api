from flask_restful import Resource, request
from models.models import Workers
from server import db
from serializers.workers import worker_schema, workers_schema

class WorkersListController(Resource):
    
    def get(self):
        worker = Workers.query.all()
        return {"data": workers_schema.dump(worker), "message": "exito"}

    def post(self):
        data = {
            "nombres": request.json['nombres'],
            "apellidos": request.json['apellidos'],
            "puesto": request.json['puesto'],
        }
        new_worker = Workers(**data)
        db.session.add(new_worker)
        db.session.commit()
        return {'data': worker_schema.dump(new_worker)}


class WorkerController(Resource):
    def get(self, pk):
        worker = Workers.query.get(pk)
        if not worker:
            return {"Mensaje":"No se encontro el trabajador"}, 404
        single_worker = []
        single_worker.append(worker.to_json())
        return {'Worker':worker_schema.dump(worker)}
        
    def put(self, pk):
        worker = Workers.query.get(pk)
        if not worker:
            return {"mensaje":"No se encontro el trabajador"}, 404
        data = {
            "nombres": request.json['nombres'],
            "apellidos": request.json['apellidos'],
            "puesto": request.json['puesto'],
        }
        worker.nombres = data["nombres"]
        worker.apellidos = data["apellidos"]
        worker.puesto = data["puesto"]
        
        db.session.add(worker)
        db.session.commit()
        return {"Trabajador": worker_schema.dump(worker),"mensaje":"actualizado"}
    
    def delete(self,pk):
            worker = Workers.query.get(pk)
            if not worker:
                return {"mensaje":"No se encontro el trbabajdor"}
            db.session.delete(worker)
            db.session.commit()
            return {"Trabajador": worker_schema.dump(worker),"mensaje":"Eliminado"}
