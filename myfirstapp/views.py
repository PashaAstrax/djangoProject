from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import DBUtils

class UserListCreateView(APIView):

    def get(self, *args, **kwargs):
        users = DBUtils.read_db()
        return Response(users)

    def post(self, *args, **kwargs):
        user = self.request.data
        created_user = DBUtils.create(user)
        return Response(created_user)

class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        users = DBUtils.read_db()
        for user in users:
            if user.get("id") == pk:
                return Response(user)
        return Response("User with this id is not found")

    def patch(self, *args, **kwargs):
        pk = kwargs.get("pk")
        data = self.request.data
        user = DBUtils.update(data, pk)
        if not user:
            return Response("User with this id is not found")
        return Response(user)

    def delete(self, *args, **kwargs):
        pk = kwargs.get("pk")
        is_delete = DBUtils.delete(pk)
        if not is_delete:
            return Response("User with this id is not found")
        return Response("deleted")


