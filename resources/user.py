from flask_restful import Resource
from users import users
from flask import request


class UserList(Resource):
    def get(self):
        """
        Obtiene la lista de usuarios.

        ---
        tags:
        - Users
        responses:
          200:
            description: Lista de usuarios obtenida correctamente
            schema:
              type: object
              properties:
                results:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: ID del usuario
                      name:
                        type: string
                        description: Nombre del usuario
                      email:
                        type: string
                        format: email
                        description: Correo electrónico del usuario
                      age:
                        type: integer
                        description: Edad del usuario
        """
        return {'results': users}
    
    """
    Clase para manipular la lista de usuarios.

    ---
    tags:
      - Users
    parameters:
      - in: body
        name: user
        schema:
          id: User
          required:
            - name
            - email
            - age
          properties:
            id:
              type: integer
              description: ID del usuario
            name:
              type: string
              description: Nombre del usuario
            email:
              type: string
              format: email
              description: Correo electrónico del usuario
            age:
              type: integer
              description: Edad del usuario
    responses:
      201:
        description: Usuario creado correctamente
    """
    def post(self):
        """
        Crea un nuevo usuario.

        ---
        tags:
        - Users
        consumes:
          - application/json
        parameters:
          - in: body
            name: user
            description: Usuario a crear
            schema:
              id: User
              required:
                - name
                - email
                - age
              properties:
                id:
                  type: integer
                  description: ID del usuario
                name:
                  type: string
                  description: Nombre del usuario
                email:
                  type: string
                  format: email
                  description: Correo electrónico del usuario
                age:
                  type: integer
                  description: Edad del usuario
        responses:
          201:
            description: Usuario creado correctamente
        """
        data = request.json
        last_user_id = users[-1].get('id')
        new_user = {"id": last_user_id + 1, **data}
        users.append(new_user)

        return {'results': users}, 201
    
class User(Resource):

    def get(self, id):
        """
        Obtiene un usuario por su ID.

        ---
        tags:
        - Users
        produces:
          - application/json
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: ID del usuario a consultar
        responses:
          200:
            description: Usuario obtenido correctamente
            schema:
              type: object
              properties:
                results:
                  type: object
                  properties:
                    id:
                      type: integer
                      description: ID del usuario
                    name:
                      type: string
                      description: Nombre del usuario
                    email:
                      type: string
                      format: email
                      description: Correo electrónico del usuario
                    age:
                      type: integer
                      description: Edad del usuario
          404:
            description: Usuario no encontrado
    """
        user = next(filter(lambda x: x['id'] == id, users), None)

        if user is None:
            return {'message': 'User not found'}, 404
        return {'results': user}
    
    def put(self, id):
        """
    Actualiza un usuario por su ID.

    ---
    tags:
      - Users
    produces:
      - application/json
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del usuario a actualizar
      - in: body
        name: user
        description: Datos del usuario a actualizar
        required: true
        schema:
          id: User
          properties:
            name:
              type: string
              description: Nuevo nombre del usuario
            email:
              type: string
              format: email
              description: Nuevo correo electrónico del usuario
            age:
              type: integer
              description: Nueva edad del usuario
    responses:
      200:
        description: Usuario actualizado correctamente
        schema:
          type: object
          properties:
            results:
              type: object
              properties:
                id:
                  type: integer
                  description: ID del usuario
                name:
                  type: string
                  description: Nombre actualizado del usuario
                email:
                  type: string
                  format: email
                  description: Correo electrónico actualizado del usuario
                age:
                  type: integer
                  description: Edad actualizada del usuario
      404:
        description: Usuario no encontrado
    """
        data = request.json
        user = None
        for i, u in enumerate(users):
            if u['id'] == id:
                user = u
                users[i] = {**user, **data}  # Actualiza el usuario con los datos recibidos
                user = users[i]
                break

        if user is None:
            return {'message': 'User not found'}, 404

        return {'results': user}
    
    def delete(self, id):
        """
    Elimina un usuario por su ID.

    ---
    tags:
      - Users
    produces:
      - application/json
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del usuario a eliminar
    responses:
      200:
        description: Usuario eliminado correctamente
        schema:
          type: object
          properties:
            message:
              type: string
              description: Mensaje de confirmación de eliminación
      404:
        description: Usuario no encontrado
    """
        user = None
        for i, u in enumerate(users):
            if u['id'] == id:
                user = users.pop(i)

        if user is None:
            return {'message': 'User not found'}, 404
        return {'message': 'User deleted'}
        
        """
        Obtiene un usuario por su ID.

        ---
        parameters:
            - id : id
        
        responses:
            200:
                description: Usuario obtenido correctamente
                schema:
                    type: object
                    properties:
                        results:
                            type: object
                            properties:
                                id:
                                    type: integer
                                    description: ID del usuario
                                name:
                                    type: string
                                    description: Nombre del usuario
                                email:
                                    type: string
                                    format: email
                                    description: Correo electrónico del usuario
                                age:
                                    type: integer
                                    description: Edad del usuario
            404:
                description: Usuario no encontrado
        """