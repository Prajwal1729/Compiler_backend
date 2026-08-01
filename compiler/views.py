from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .utils.code_executor import *
EXECUTORS = {
    "python": runPython,
    "nodejs": runNode,
    "java": runJava,
    "c": runC,
    "cpp": runCpp,
    "ruby": runRuby,
    "go": runGo,
    "php": runPhp,
    "typescript": runTypescript,
    "csharp": runCsharp
}

import subprocess,logging
logger = logging.getLogger('compiler')

# Create your views here.

# create your backend apis here

# for testing purpose only, you can remove this later #
# def test_code(request):
#     message = request.data.get('message')

#     return Response({'message': f"Recieved message: {message}"})

# user registration api
@api_view(['POST'])

def signUp(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        logger.info(f"Received signup request with email: {email}")
        if not email or not password:
            return Response({
                "success": False,
                "message": "Email and password are required",
                "email": email,
                "password": password
            }, status=400)

        if User.objects.filter(email=email).exists():
            return Response({
                "success": False,
                "message": "User already exists",
                "email": email
            }, status=400)

        User.objects.create_user(
            email=email,
            password=password
        )

        return Response({
            "success": True,
            "message": "User created successfully",
            "email": email
        }, status=200)
    
    except Exception as e:
        return Response({
            "error": str(e)
        })


# user login api
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    try:
        email = request.data.get('email')
        password = request.data.get('password')

        logger.info(f"Login request:{email}")

        if not email or not password:
            return Response({
                "success":False,
                "message": "Email and Password is required."
            }, status=400)

        user = authenticate(username=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)

            return Response({
                "success": True,
                "message": "LoggedIn Successfully",
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=200)
        

        return Response({
            "success": False,
            "message": "Invalid Credentials"
        }, status=200)

    except Exception as e:
        return Response({
            "error": str(e)
        })
    


@api_view(['GET']) 
@permission_classes([AllowAny]) 
def languagesList(request):
    languages = [
        {
            "name": "python",
            "template": 'print("Hello World")'
        },
        {
            "name": "nodejs",
            "template": 'console.log("Hello World");'
        },
        {
            "name": "java",
            "template": """public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}"""
        },
        {
            "name": "c",
            "template": """#include <stdio.h>

int main() {
    printf("Hello World");
    return 0;
}"""
        },
        {
            "name": "cpp",
            "template": """#include <iostream>
using namespace std;

int main() {
    cout << "Hello World";
    return 0;
}"""
        },
        {
            "name": "ruby",
            "template": 'puts "Hello World"'
        },
        {
            "name": "go",
            "template": """package main
import "fmt"

func main() {
    fmt.Println("Hello World")
}"""
        },
        {
            "name": "php",
            "template": """<?php
echo "Hello World";
?>"""
        },
        {
            "name": "typescript",
            "template": 'console.log("Hello World");'
        },
        {
            "name": "csharp",
            "template": """using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello World");
    }
}"""
        }
    ]
    return Response({
        "success": True,
        "languages": languages
    })

@api_view(['POST'])
def runCode(request):
    code = request.data.get('code')
    language = request.data.get('language')

    executors = EXECUTORS.get(language)
    
    if not executors:
        return Response({
            "error": "Language not supported."
        })
    
    try:
        output = executors(code)
        return Response({
            "output": output
        })
    except Exception as e:
        return Response({
            "error": str(e)
        })

    

    

    
    
