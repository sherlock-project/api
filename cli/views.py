import os
from subprocess import *

from rest_framework.response import Response
from rest_framework.views import APIView

from helper import *
import json
from django.http import HttpResponse, JsonResponse

class CliView(APIView):
    """Pass in command directly to sherlock."""
    def post(self, request):
        data = json.loads(request.body)
        args = data['args']

        if valid_args(args) == False:
            output = "Invalid argument string"
        else:
            full_cmd = f"{py_command()} {sherlock_dir()}/sherlock {args}"
            proc = Popen(full_cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
            outs, errs = proc.communicate()
            output = outs if outs else errs

        return Response({'output': output})

class DataView(APIView):
    """Request JSON data from sherlock resources."""
    def get(self, request):
        return Response(sherlock_data())
