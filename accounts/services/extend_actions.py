from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


class ExtendActions:
    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response(
            {'detail': 'This endpoint is disabled'},
            status= status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    @extend_schema(exclude=True)
    def create(self, request, *args, **kwargs):
        return Response(
            {'detail': 'This endpoint is disabled'},
            status= status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return Response(
            {'detail': 'This endpoint is disabled'},
            status= status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kwargs):
        return Response(
            {'detail': 'This endpoint is disabled'},
            status= status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    @extend_schema(exclude=True)
    def destroy(self, request, *args, **kwargs):
        return Response(
            {'detail': 'This endpoint is disabled'},
            status= status.HTTP_405_METHOD_NOT_ALLOWED,
        )