import socket, json
from django.db.models import Q

from automobile.models import Automobile
from config.settings import MCP_HOST, MCP_PORT


class McpServer:
    help = "Start the MCP server"

    def handle(self, *args, **kwargs):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((MCP_HOST, MCP_PORT))
        server.listen(5)

        print(f"Server running on {MCP_HOST}:{MCP_PORT}")

        while True:
            conn, addr = server.accept()
            print(f"Conection received from {addr}")

            data = conn.recv(1024).decode('utf-8')
            if not data:
                continue

            filters = json.loads(data)
            automobiles = self.search_automobiles(**filters)
            conn.send(json.dumps(automobiles).encode('utf-8'))
            conn.close()

    def search_automobiles(self, **kwargs):        
        filters = Q()

        if 'model' in kwargs:
            filters &= Q(model__icontains=kwargs['model'])

        if 'color' in kwargs:
            filters &= Q(color__icontains=kwargs['color'])

        if 'brand' in kwargs:
            filters &= Q(brand__icontains=kwargs['brand'])

        if 'engine' in kwargs:
            filters &= Q(engine__icontains=kwargs['engine'])

        if 'transmission' in kwargs:
            filters &= Q(transmission__icontains=kwargs['transmission'])

        if 'fuel_type' in kwargs:
            filters &= Q(fuel_type__icontains=kwargs['fuel_type'])

        if 'num_doors' in kwargs:
            filters &= Q(num_doors=kwargs['num_doors'])

        if 'num_seats' in kwargs:
            filters &= Q(num_seats=kwargs['num_seats'])

        if 'year' in kwargs:
            filters &= Q(year=kwargs['year'])

        if 'mileage' in kwargs:
            filters &= Q(mileage__lte=kwargs['mileage']) 
        
        automobiles = Automobile.objects.filter(filters).order_by('-created_at')
        
        return list(automobiles.values('id'))
        
        return [
            {
                'model': automobile.model, 'brand': automobile.brand, 'color': automobile.color,
                'fuel_type': automobile.fuel_type,
                'year': automobile.year, 'mileage': float(automobile.mileage),
                'price': float(automobile.price if automobile.price else 0)
            } 
            for automobile in automobiles
        ]
