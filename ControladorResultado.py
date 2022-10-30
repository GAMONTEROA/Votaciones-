from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato

from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioResultado.findAll()
    """
    Asignacion candidato y mesa a resultado
    """
    def create(self,infoResultados,id_candidato,id_mesa):
        nuevoResultado = Resultado(infoResultados)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.repositorioResultado.save(nuevoResultado)

    def show(self,id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de inscripción (estudiante y materia)
    """
    def update(self,id,infoResultados,id_candidato,id_mesa):
        elResultado =Resultado(self.repositorioResultado.findById(id))
        elResultado.votoscandidato=infoResultados["votoscandidato"]
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    "Obtener votos por candidato por mesa"
    def votosporCandidato(self,id_mesa,id_candidato):
        return self.repositorioResultado.getListadoVotosporCandidato(id_mesa,id_candidato)

    "Obtener mesas con mayor participacion"
    def mesasMayorParticipacion(self):
        return self.repositorioResultado.getListadoMesasMayorParticipacion()

    "Obtener distribucion congreso por partido politico"
    def votosporPartido(self,id_partido):
        return self.repositorioResultado.getListadoporPartido(id_partido)