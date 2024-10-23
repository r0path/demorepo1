from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import logging
import shlex

def process_command(request):
    # Get user input safely
    user_input = request.GET.get('command', '')
    
    # Log the request 
    logging.info(f"Received command request: {user_input}")
    

    # Execute command safely
    try:
        sanitized_input = shlex.quote(user_input)
        output = subprocess.check_output(sanitized_input, shell=True, text=True)
        return HttpResponse(output)
    except subprocess.CalledProcessError:
        return HttpResponse("Error executing command")
