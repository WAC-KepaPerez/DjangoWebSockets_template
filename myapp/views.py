from django.shortcuts import render

# Create your views here.
import markdown
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloView(APIView):
    def get(self, request):
        # Lógica de la vista
        # Puedes pasar datos a tu plantilla si es necesario
        # context = {
        #     'titulo': 'Hello this is home',
        #     'mi_clase': 'mi-clase-css',  # Clase CSS que deseas agregar
        # }
        with open('./readme.md', 'r') as file:
            md_content = file.read()

        # Convert MD to HTML
        html_content = markdown.markdown(md_content)

        # Pass the HTML content to the template
        context = {'html_content': html_content}

        # Render the template
        return render(request, 'md_template.html', context)
    
class Example(APIView):
    def get(self, request):
        return render(request, 'example.html')


