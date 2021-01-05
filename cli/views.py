import os
from subprocess import *

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView

from helper import *
import json

class CliView(APIView):
    """Pass in command directly to sherlock."""
    def post(self, request):
        data = json.loads(request.body)
        print(data['args'])
        full_cmd = f"{py_command()} {sherlock_dir()}/sherlock {data['args']}"
        proc = Popen(full_cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        outs, errs = proc.communicate()
        output = outs if outs else errs
        return Response({'output': output})
