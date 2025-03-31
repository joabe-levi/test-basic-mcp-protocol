import socket, json

from automobile.models import Automobile
from config.settings import MCP_HOST, MCP_PORT


class ClienteMCP:

    def buscar_veiculos(self, **kwargs):
        """Envia os filtros para o servidor MCP e retorna os resultados."""
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((MCP_HOST, MCP_PORT))

            client.send(json.dumps(kwargs).encode('utf-8'))
            data = client.recv(4096).decode('utf-8')
            client.close()

            values = json.loads(data)
            ids = [item.get('id') for item in values]
            return Automobile.objects.filter(id__in=ids).order_by('-created_at')
        
        except Exception as e:
            print(f"Error to search automobiles: {e}")
            return []
