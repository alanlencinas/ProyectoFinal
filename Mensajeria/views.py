# messenger/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensajeria
from django.contrib import messages
from django.contrib.auth.models import User
from AppCoder.views import *
from django.shortcuts import render, get_object_or_404

@login_required
@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        content = request.POST.get('contenido')
        asunt = request.POST.get('asunto')
        sender = request.user
        receiver_id = request.POST.get('receiver_id')  # Obtiene el destinatario del formulario
        if receiver_id:
            receiver = User.objects.get(pk=receiver_id)
            message = Mensajeria.objects.create(emisor=sender, receptor=receiver, contenido=content, asunto=asunt)
            messages.success(request, 'Mensaje enviado exitosamente!')
            return redirect('inbox')
        else:
            messages.error(request, 'Debes seleccionar un destinatario.')
    else:
        # Recupera la lista de usuarios para mostrar en el formulario
        users = User.objects.exclude(id=request.user.id)  # Excluye al usuario actual
        return render(request, 'Mensajeria/enviar_mensaje.html', {'users': users, "avatar": obtenerAvatar(request)})
    
    
@login_required
def inbox(request):
    messages = Mensajeria.objects.all()  # Otra lógica para obtener los mensajes
    return render(request, 'Mensajeria/inbox.html', {'messages': messages, 'avatar': obtenerAvatar(request)})




def view_message(request, message_id):
    # Obtener el mensaje específico o mostrar una página de error 404 si no existe
    mensaje = get_object_or_404(Mensajeria, pk=message_id)
    
    # Aquí puedes agregar lógica adicional si es necesario, como marcar el mensaje como leído, etc.

    return render(request, 'Mensajeria/inbox.html', {'message': mensaje, 'avatar': obtenerAvatar})


