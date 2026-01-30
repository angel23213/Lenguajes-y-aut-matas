class AutomataVehiculoMinimal:
    def __init__(self):
        self.estado_actual = "Apagado"
        self.transiciones = {
            ("Apagado", "encender"): "Encendido",
            ("Apagado", "activar_alarma"): "Alarma",
            ("Alarma", "desactivar_alarma"): "Apagado",
            ("Encendido", "acelerar"): "En movimiento",
            ("Encendido", "apagar"): "Apagado",
            ("En movimiento", "frenar"): "Encendido",
        }
    
    def mostrar_estado(self):
        print(f"\nEstado actual: {self.estado_actual}")
    
    def eventos_disponibles(self):
        eventos = []
        for (estado, evento) in self.transiciones:
            if estado == self.estado_actual:
                eventos.append(evento)
        return eventos
    
    def transicionar(self, evento):
        clave = (self.estado_actual, evento)
        if clave in self.transiciones:
            self.estado_actual = self.transiciones[clave]
            return True
        return False


def main():
    automata = AutomataVehiculoMinimal()
    
    print("Autómata Básico de Vehículo")
    print("Eventos: encender, apagar, acelerar, frenar, activar_alarma, desactivar_alarma")
    print("Salir: escribir 'salir'")
    
    while True:
        automata.mostrar_estado()
        eventos = automata.eventos_disponibles()
        
        if not eventos:
            print("Estado terminal alcanzado. Fin del programa.")
            break
        
        print(f"Eventos disponibles: {', '.join(eventos)}")
        
        evento = input("\nIngresa evento: ").strip().lower()
        
        if evento == "salir":
            print("Programa terminado.")
            break
        
        if evento in eventos:
            if automata.transicionar(evento):
                print(f"✓ Transición realizada")
            else:
                print("✗ Error en transición")
        else:
            print("✗ Evento no disponible desde este estado")


if __name__ == "__main__":
    main()