class ValidadorAutomata:
    def __init__(self):
        # Tabla de transiciones simplificada
        self.transiciones = {
            'q0': {'a': 'q1', 'b': 'q2'},
            'q1': {'a': 'q1', 'b': 'q1'},
            'q2': {'a': 'q0', 'b': 'q2'}
        }
        self.estados_finales = {'q1', 'q2'}
    
    def validar(self, palabra):
        estado = 'q0'  # Estado inicial
        
        for simbolo in palabra:
            if simbolo not in {'a', 'b'}:
                return False  # Símbolo inválido
            if simbolo in self.transiciones[estado]:
                estado = self.transiciones[estado][simbolo]
            else:
                return False  # Transición no definida
        
        return estado in self.estados_finales


def main():
    print("="*40)
    print("AUTÓMATA")
    print("="*40)
    print("\nIngresa palabras con 'a' y 'b'")
    print("Ejemplo: abbb, bbba, a, b, ab, ba")
    print("="*40)
    
    validador = ValidadorAutomata()
    
    while True:
        palabra = input("\nPalabra a validar: ").strip().lower()
        
        if validador.validar(palabra):
            print(f"✓ PALABRA VÁLIDA")
        else:
            print(f"✗ PALABRA NO VÁLIDA")
        
        otra = input("\n¿Otra palabra? (s/n): ").lower()
        if otra not in ['s', 'si']:
            break
    
    print("\n¡Hasta luego!")


if __name__ == "__main__":
    main()