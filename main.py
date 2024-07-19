import json

#para encontar el archivo
def listadedatos():
    with open("alumnos.json", "r") as file:
         return json.load(file)
#donde se sobre escriben los archivos 
def datosexistentes(informacion):
     with open("alumnos.json", "w") as file:
        json.dump(informacion, file , indent=4)
    
def alumnos(cedula):
    with open("alumnos.json", "r") as file:
        content=json.load(file)
    for estudiante in content["alumnos"]:
        if estudiante [cedula]==cedula:
            return estudiante
    

#datos de alumnnos.json
def editar_estudiantes(estudiante):
    print("cedula: " , estudiante["cedula"] , "nombre:" , estudiante["nombre"] , "apellido:" , estudiante["apellido"] ,
         "nota", estudiante["nota"] )
    #pedir datos
    estudiante["nombre"]=input("Nombre nuevo")
    estudiante["apellido"]=input("apellido nuevo")
    estudiante["notas"]=input("notas actualizadas")
    #actualizados
    print("cedula: " , estudiante["cedula"] , "nombre:" , estudiante["nombre"] , "apellido:" , estudiante["apellido"] ,
         "nota", estudiante["nota"])
    
informacion=listadedatos
cedula=input("escriba la cedula del alumno:")
estudiante=alumnos(cedula)


      
        