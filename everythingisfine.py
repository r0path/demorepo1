from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import logging

def process_command(request):
    # Get user input safely
    user_input = request.GET.get('command', '')
    
    # Log the request 
    logging.info(f"Received command request: {user_input}")
    

    # Execute command safely
    try:
        output = subprocess.check_output([user_input], shell=False)
        return HttpResponse(output)
    except subprocess.CalledProcessError:
        return HttpResponse("Error executing command")
