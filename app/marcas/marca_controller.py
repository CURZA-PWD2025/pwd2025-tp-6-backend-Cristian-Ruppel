from app.marcas.marca_model import MarcaModel

class MarcaController:
    @staticmethod
    def get_all():
        try:
            return MarcaModel.get_all()
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def get_one(id):
        try:
            marca = MarcaModel.get_one(id)
            return marca if marca else {'error': 'Marca no encontrada'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def create(data):
        try:
            if not data.get('nombre'): 
                return {'error': 'Nombre es requerido'}
            marca = MarcaModel.deserializar(data)
            return {'success': True, 'id': marca.id} if marca.create() else {'error': 'Error al crear'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def update(data):
        try:
            if not data.get('id'):
                return {'error': 'ID es requerido'}
            marca = MarcaModel.deserializar(data)
            return {'success': True} if marca.update() else {'error': 'Error al actualizar'}
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def delete(id):
        try:
            return {'success': True} if MarcaModel.delete(id) else {'error': 'Error al eliminar'}
        except Exception as e:
            return {'error': str(e)}