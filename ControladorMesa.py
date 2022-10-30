from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa
class ControladorMesa():

    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevaMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)
    def show(self,id):
        laMesa=Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__
    def update(self,id,infoMesa):
        MesaActual=Mesa(self.repositorioMesa.findById(id))
        MesaActual.nummesa=infoMesa["nummesa"]
        MesaActual.numinscritos = infoMesa["numinscritos"]
        return self.repositorioMesa.save(MesaActual)
    def delete(self,id):
        return self.repositorioMesa.delete(id)