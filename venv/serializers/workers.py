from marshmallow import Schema


class WorkerSchema(Schema):

    class Meta:
        fields = ('id_empleado','nombres', 'apellidos', 'puesto')
        ordered = True


workers_schema = WorkerSchema(many=True)
worker_schema = WorkerSchema()