from service.cliente_service import ClienteService
from service.supervisor_service import SupervisorService
from service.menu_service import MenuService
from modelo.supervisor_zona import SupervisorZona

def main():
    #Creando instancias para acceder
    menu_service = MenuService()
    supervisor_service = SupervisorService()
    cliente_service = ClienteService()
    
    while True:
        menu_service.imprimir_menu() #Imprimiendo menu
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1":
                cliente_service.crear_cliente()
            case "2":
                supervisor_service.crear_supervisor()
            case "3":
                print("Saliendo del Programa")
                break
            case _:
                print("Opcion invalida")

# Funcion inicializadora para darle un punto de entrada/inicio al programa
if __name__ == "__main__":

    supervisor_zona = SupervisorZona('Maria','Guadalupe','1-9','tech','5','7','7')
    print(supervisor_zona.apellido)
    print(supervisor_zona._promedio)













