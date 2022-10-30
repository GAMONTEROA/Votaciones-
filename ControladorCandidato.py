from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido

class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido=RepositorioPartido()

    def index(self):
        print("Listar todos los candidatos")
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        print("Crear un candidato")
        elCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(elCandidato)

    def show(self, id):
        print("Mostrando un candidato con id ", id)
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        print("Actualizando candidato con id ", id)
        CandidatoActual = Candidato(self.repositorioCandidato.findById(id))
        CandidatoActual.cedula = infoCandidato["cedula"]
        CandidatoActual.numresolucion = infoCandidato["numresolucion"]
        CandidatoActual.nombre = infoCandidato["nombre"]
        CandidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(CandidatoActual)

    def delete(self, id):
        print("Eliminando candidato con id ", id)
        return self.repositorioCandidato.delete(id)

    """
    Relación Candidato y Partido
    """

    def asignarPartido(self,id,id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)