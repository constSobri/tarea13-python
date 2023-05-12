import sqlite3


def main():
    def esAlumno():
        login = input('El alumno esta registrado? (S/N/VER LISTA)')
        if login == 'S':
            busqueda()
            otraVez()
        elif login == 'N':
            registrate()
            otraVez()
        elif login == 'VER LISTA':
            con = sqlite3.connect('Alumnos.db', isolation_level=None)
            cursor = con.cursor()

            lista = cursor.execute('SELECT * FROM Alumnos')

            for alumnos in lista:
                print(f'N. {alumnos[0]}\nNombre: {alumnos[1]}\nApellido: {alumnos[2]}\n')

            cursor.close()
            con.close()

            return esAlumno()
        else:
            print("Por favor indica la respuesta con una S o N mayuscula.")
            esAlumno()

    def otraVez():
        denuevo = input('Desea hacer otra busqueda o registro? (S/N)')

        if denuevo == 'S':
            esAlumno()
        elif denuevo == 'N':
            return
        else:
            print('No se detecto la respuesta, por favor escribe S o N en mayusculas. Intentalo de nuevo.')
            otraVez()

    def nuevoID():
        con = sqlite3.connect('Alumnos.db', isolation_level=None)
        cursor = con.cursor()
        new_id = 0

        cursor.execute('SELECT MAX(id) FROM Alumnos')
        last_id = cursor.fetchone()[0]

        if last_id is None:
            new_id = 1
        else:
            new_id = last_id + 1

        cursor.close()
        con.close()

        return new_id

    def registrate():
        nombre = input('Escribe el nombre: ')
        apellido = input('Escribe el apellido: ')
        con = sqlite3.connect('Alumnos.db', isolation_level=None)
        cursor = con.cursor()

        query = f'INSERT INTO Alumnos(id,nombre,apellido) VALUES({nuevoID()},"{nombre}","{apellido}")'

        cursor.execute(query)

        cursor.close()
        con.close()

        def seguir():
            respuesta = input('Desea seguir registrando? (S/N)')
            if respuesta == 'S':
                registrate()
            elif respuesta == 'N':
                bus = input('Desea hacer una búsqueda? (S/N)')
                if bus == 'S':
                    busqueda()
                else:
                    return quit()
            else:
                print('No se detecto la respuesta, por favor escribe S o N en mayusculas. Intentalo de nuevo.')
                return seguir()

        seguir()

    def busqueda():
        nombre = input('Escribe el nombre: ')
        con = sqlite3.connect('Alumnos.db')
        cursor = con.cursor()

        query = f'SELECT * FROM Alumnos WHERE nombre="{nombre}"'

        data = cursor.execute(query)

        if data is None:
            print('No se encontro el usuario, por favor volver a intentarlo.')
            return verificado()
        else:
            for Alumnos in data:
                print(f'N. {Alumnos[0]}\nNombre: {Alumnos[1]}\nApellido: {Alumnos[2]}')

        cursor.close()
        con.close()

    esAlumno()


if __name__ == '__main__':
    main()
