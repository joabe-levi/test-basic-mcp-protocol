from mcp.client.client import ClienteMCP


class VirtualAgent:
    
    def collect_filter(self):
        print("\n🤖 Olá! Vamos encontrar o veículo ideal para você!\n")
        
        model = input("Digite o modelo do veículo (ou pressione Enter para ignorar): ").strip()
        color = input("Digite a cor do veículo (ou pressione Enter para ignorar): ").strip()
        brand = input("Digite a marca do veículo (ou pressione Enter para ignorar): ").strip()
        engine = input("Digite o tipo de motor (ou pressione Enter para ignorar): ").strip()
        transmission = input("Digite o tipo de transmissão (manual/automática, ou Enter para ignorar): ").strip()
        fuel_type = input("Digite o tipo de combustível (gasolina/diesel/etanol/etc., ou Enter para ignorar): ").strip()
        num_doors = input("Digite o número de portas (ou pressione Enter para ignorar): ").strip()
        num_seats = input("Digite o número de assentos (ou pressione Enter para ignorar): ").strip()
        year = input("Digite o ano do veículo (ou pressione Enter para ignorar): ").strip()
        mileage = input("Digite a quilometragem máxima (ou pressione Enter para ignorar): ").strip()

        filtros = {}

        if model:
            filtros['model'] = model
            
        if color:
            filtros['color'] = color
            
        if brand:
            filtros['brand'] = brand
            
        if engine:
            filtros['engine'] = engine
            
        if transmission:
            filtros['transmission'] = transmission
            
        if fuel_type:
            filtros['fuel_type'] = fuel_type
            
        if num_doors.isdigit():
            filtros['num_doors'] = int(num_doors)
            
        if num_seats.isdigit():
            filtros['num_seats'] = int(num_seats)
            
        if year.isdigit():
            filtros['year'] = int(year)
            
        if mileage.isdigit():
            filtros['mileage'] = int(mileage)

        return filtros
    
    def results(self, automobiles):
        if not automobiles:
            print("\n❌ Nenhum veículo encontrado.")
            return

        print("\n✅ Veículos encontrados:")
        for automobile in automobiles:
            print(
                f"""
                Modelo: {automobile.model}
                Marca: {automobile.brand}
                Cor: {automobile.color}
                Combustível: {automobile.fuel_type}
                Ano: {automobile.year}
                Quilometragem: {automobile.mileage}
                Preço: {automobile.price}
                """
            )
            
    def start(self):
        cliente = ClienteMCP()

        while True:
            filtros = self.collect_filter()
            veiculos = cliente.buscar_veiculos(**filtros)
            self.results(veiculos)

            continuar = input("\nDeseja fazer outra busca? (s/n): ").strip().lower()
            if continuar != 's':
                print("\n👋 Obrigado por usar o assistente virtual. Até logo!")
                break
