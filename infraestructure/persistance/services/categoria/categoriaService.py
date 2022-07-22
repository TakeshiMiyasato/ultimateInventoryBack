from datetime import datetime

from django.db import transaction
from pymitter import EventEmitter
from rest_framework import serializers
from rest_framework.response import Response

from infraestructure.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class CategoriaService:

    def getAllCategorias(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def getCategoriasById(self, request):
        categorias = Categoria.objects.get(pk=request.data['id'])
        serializer = CategoriaSerializer(categorias, many=False)
        return Response(serializer.data)

    def createCategoria(self, obj_categoria, event_handler):
        categoria = Categoria()
        categoria.nombre = obj_categoria.nombre
        categoria.save()
        serializer = CategoriaSerializer(categoria, many=False)
        return Response(serializer.data)

    def updateCategoria(self, request, obj_categoria, event_handler):
        categoria = Categoria.objects.get(pk=request.data['id'])
        categoria.nombre = obj_categoria.nombre
        categoria.fechaLastUpdate = datetime.now()
        categoria.save()

        serializer = CategoriaSerializer(categoria, many=False)

        return Response(serializer.data)