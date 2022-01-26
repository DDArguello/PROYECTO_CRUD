class Departamento:
    secuencia=2
    departamentos = [ {"codigo":1,"departamento":"Sistemas"},
              {"codigo":2,"departamento":"Logistica"},
             ]
    
    def __init__(self,descrip):
        Departamento.secuencia +=1
        self.codigo=Departamento.secuencia
        self.departamento=descrip
    
    def registro(self):
        return {"codigo":self.codigo,"departamento":self.departamento}


        