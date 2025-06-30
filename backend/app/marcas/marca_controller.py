from app.marcas.marca_model import MarcaModel

class MarcaController:
    @staticmethod
    def get_all():
        try:
            marcas = MarcaModel.get_all()
            return [m.serializar() for m in marcas] if marcas else []
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def get_one(id):
        try:
            if marca := MarcaModel.get_one(id):
                return marca.serializar()
            return {'error': 'Marca no encontrada', 'status': 404}
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def create(data):
        try:
            if not data.get('nombre'):
                return {'error': 'Nombre es requerido', 'status': 400}
            marca = MarcaModel.deserializar(data)
            if marca.create():
                return {'success': True, 'id': marca.id, 'status': 201}
            return {'error': 'Error al crear marca', 'status': 400}
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def update(data):
        try:
            if not data.get('id'):
                return {'error': 'ID es requerido', 'status': 400}
            marca = MarcaModel.deserializar(data)
            if marca.update():
                return {'success': True, 'status': 200}
            return {'error': 'Error al actualizar marca', 'status': 400}
        except Exception as e:
            return {'error': str(e), 'status': 500}

    @staticmethod
    def delete(id):
        try:
            if MarcaModel.delete(id):
                return {'success': True, 'status': 200}
            return {'error': 'Error al eliminar marca', 'status': 400}
        except Exception as e:
            return {'error': str(e), 'status': 500}