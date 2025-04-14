from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
import requests
import os
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from core.faqs import buscar_resposta_faq,FAQS
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
load_dotenv()


@ensure_csrf_cookie
def csrf_cookie(request):
    return JsonResponse({'detail': 'CSRF cookie set'})

@csrf_exempt
def register(request):
    if request.method == 'POST':        
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body) 
                form = CustomUserCreationForm(data)  
            except json.JSONDecodeError:
                return JsonResponse({"error": "JSON inválido"}, status=400)
        else:
            form = CustomUserCreationForm(request.POST)  
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({"message": "Cadastro realizado com sucesso!", "user": user.username}, status=201)
        else:
            return JsonResponse({"errors": form.errors}, status=400)

    
    form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})


def home(request):
    return render(request, 'core/index.html')

#@csrf_exempt#Para os testes no Postman retirar este comentário, para desativação do token CSRF
    if request.method == 'POST':
        # Verifica se a requisição tem um corpo JSON
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)  # Converte JSON para dicionário Python
                form = CustomUserCreationForm(data)  # Passa os dados para o formulário
            except json.JSONDecodeError:
                return JsonResponse({"error": "JSON inválido"}, status=400)
        else:
            form = CustomUserCreationForm(request.POST)  # Se não for JSON, usa POST normal
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({"message": "Cadastro realizado com sucesso!", "user": user.username}, status=201)
        else:
            return JsonResponse({"errors": form.errors}, status=400)

    # Se for uma requisição GET, exibe o formulário normalmente (para quem acessa via navegador)
    form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

from django.contrib.auth import get_user_model

User = get_user_model()

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                email = data.get('email')
                password = data.get('password')

                try:
                    # Busca o usuário pelo e-mail e pega o username
                    user_obj = User.objects.get(email=email)
                    username = user_obj.username
                except User.DoesNotExist:
                    return JsonResponse({'errors': {'email': 'Usuário não encontrado.'}}, status=401)

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return JsonResponse({'message': 'Login realizado com sucesso!','user': user.username }, status=200)
                else:
                    return JsonResponse({'errors': {'password': 'Senha incorreta.'}}, status=401)
            else:
                return JsonResponse({'error': 'Requisição deve ser JSON.'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

    return JsonResponse({'error': 'Método não permitido'}, status=405)


@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout realizado com sucesso!'}, status=200)
    return JsonResponse({'error': 'Método não permitido'}, status=405)


"""Testanto chatbot integrado com IA"""

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")

@ensure_csrf_cookie
def csrf_cookie(request):
    return JsonResponse({'detail': 'CSRF cookie set'})

def chatbot_page(request):
    return render(request, "core/chatbot.html")

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        try:
            
            print("✅ RECEBENDO REQUISIÇÃO /chatbot/")
            print("BODY CRU:", request.body)            
    
            data = json.loads(request.body)
            print("🧠 JSON DECODIFICADO:", data)            
            user_message = data.get("message", "").strip()
            print("🧪 Enviando à IA:", user_message.encode('utf-8'))           
            
            resposta_faq = buscar_resposta_faq(user_message)
            if resposta_faq:                
                return JsonResponse({"response": resposta_faq})      
                        
            faq_context = "Información sobre el proyecto (FAQs):\n"
            for pregunta, respuesta in FAQS.items():
                faq_context += f"- {pregunta}: {respuesta}\n"           
            
            system_message = (
                "Você é um assistente atencioso e prestativo para mães de primeira viagem. "
                "A continuación, se provee información relevante sobre el proyecto:\n\n"
                f"{faq_context}\n"
                "Usa esta información para responder de forma precisa a las preguntas relacionadas al proyecto."
            )
            
            
            response = requests.post(
                API_URL,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": user_message}
                    ]
                }
            )

            
            if response.status_code != 200:
                print("⚠️ Erro ao chamar OpenRouter:", response.text)
                return JsonResponse({"error": "Erro na resposta da IA"}, status=500)

            ai_response = response.json()
            choices = ai_response.get("choices", [])
            if not choices or "message" not in choices[0]:
                print("⚠️ Resposta inesperada:", ai_response)
                return JsonResponse({"response": "Desculpe, não consegui entender sua pergunta."}, status=200)
            
            message_content = choices[0]["message"].get("content", "").strip()
            return JsonResponse({"response": message_content})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Erro ao processar JSON da requisição."}, status=400)
        except Exception as e:
            print("❌ Erro no servidor:", str(e))
            return JsonResponse({"error": "Erro interno no servidor."}, status=500)

    return JsonResponse({"error": "Método não permitido"}, status=405)