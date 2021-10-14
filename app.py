#para exposição da api utilizei a bibliteca flask
from flask import Flask, jsonify
#para fazer a minha documentação no formato OpenAPI
from flask_pydantic_spec import FlaskPydanticSpec, Response
#Modelo de mensagem Json
from pydantic import BaseModel

server = Flask (__name__)
spec = FlaskPydanticSpec('Apresentacao', title='Apresentação Maurício')
spec.register(server)

class Perfil(BaseModel):
    nome: str
    idade: int
    local_moradia: str
    familia: str
    lazer: str
    financas: str
    academico: str
    profissional: str
    futuro: str

class ProgramadeEstagio(BaseModel):
    justificativa: str

class Programa(BaseModel):
    programa: list[ProgramadeEstagio]

class Motivo(BaseModel):
    descricao: str

class Motivadores(BaseModel):
    motivadores: list[Motivo]

class Ingram(BaseModel):
    resposta: str

class Lousa(BaseModel):
    lousa: str

@server.get('/programa')
@spec.validate(resp=Response(HTTP_200=Programa))
def programa():
    """Recupera a importância deste programa de Estágio para minha vida"""
    lista_programa = []
    lista_programa.append(ProgramadeEstagio(justificativa="O programa da oportunidade de atuar na área de desenvolvimento"))
    lista_programa.append(ProgramadeEstagio(justificativa="Da meios para realizar a minha transição de carreira"))
    lista_programa.append(ProgramadeEstagio(justificativa="Fortalece o meu crescimento profissional"))
    lista_programa.append(ProgramadeEstagio(justificativa="Colabora no desenvolvimento e aprimoramento dos meus conhecimentos em tecnologia"))
    return jsonify(Programa(programa=lista_programa).dict())

@server.get('/motivadores')
@spec.validate(resp=Response(HTTP_200=Motivadores))
def motivadores():
    """Recupera motivos para tornar-se um profissional de T.I"""
    lista_motivos = []
    lista_motivos.append(Motivo(descricao="Facilitar a vida das pessoas por meio da tecnologia"))
    lista_motivos.append(Motivo(descricao="Superar desafios"))
    lista_motivos.append(Motivo(descricao="Explorar meu raciocínio lógico"))
    lista_motivos.append(Motivo(descricao="Criar aplicações significativas"))
    return jsonify(Motivadores(motivadores=lista_motivos).dict())

@server.get('/perfil')
@spec.validate(resp=Response(HTTP_200=Perfil))
def pegar_perfil():
    """Recupera perfil do Maurício"""
    perfil=Perfil(
        nome="Maurício Helfstein Gonçalves",
        idade=27,
        local_moradia="São Paulo",
        familia="Moro com meus pais e sou muito caseiro",
        lazer="Gosto de assistir séries e filmes " +
              "além de passar o tempo com a familía",
        financas="Procuro guardar dinheiro para comprar o meu apartamento",
        academico="Cursando análise e desenvolvimento de sistemas no Mackenzie, formando em 07/2023",
        profissional="Atualmente trabalho como Assistente de produções técnicas" +
                     " na Escola Superior do Instituto Butantan",
        futuro="Planejo me desenvolver na área de T.I atuando como um especialista em dados (Data Analyst)"
    )
    return jsonify(perfil.dict())

@server.get('/ingram')
@spec.validate(resp=Response(HTTP_200=Ingram))
def pegar_resposta():
    """Recupera a resposta Porque a Ingram"""
    return jsonify(Ingram(resposta="A Ingram oferece o ambiente para aprimorar" +
                                   " os meus conhecimentos e atuar dentro de uma" +
                                   " multinacional norte americana com oportunidades" +
                                   " de crescimento e construção de networking ").dict())


@server.get('/objeto')
@spec.validate(resp=Response(HTTP_200=Lousa))
def pegar_objeto():
    """Recupera o objeto o que faz sentido na minha vida"""
    return jsonify(Lousa(lousa="A lousa é um objeto interessante na minha jornada," +
                " pois sempre gostei tirar dúvidas desde a época da escola, ensinar sobre" +
                " diversos assuntos e ministrar aulas sempre foi algo que sempre me agradou,"+
                " no trabalho quando utilizo-a nas reuniões e treinamentos retomo toda essa prática do meu passado").dict())

server.run()