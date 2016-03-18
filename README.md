LogisticRoute
=============

Descrição
=========
Sistema para calcular uma malha logística. Basicamente o sistema deve ser capaz de receber duas rotas (ponto de partida e de chegada) e a partir dessas informações calcular qual seria a melhor rota em termos de custo (gasolina por KM percorrido).
Uma malha logística segue o seguinte formato : 

        A B 10
        B D 15
        A C 20
        C D 30
        B E 50
        D E 30

Onde a primeira coluna é o ponto de partida, a segunda o pontode chegada e a terceira representa o total de KM entre um e outro.

Instalação
==========
  - Pré-requsitos: <br />
        - MongoDB <br />
        - Eve <br />
		- PyMongo <br />
        - Python 2.7 <br />
  - Instalacao : <br />
        = Toda instalação foi feita no sistema Fedora Linux release 23 = <br />
        - Instalar o python : sudo dnf install python <br />
        - Instalar o pip : sudo dnf install python-pip <br />
        - Instalar o mongoDB  : (https://docs.mongodb.org/manual/tutorial/install-mongodb-on-red-hat/) <br />
        - Iniciar o daemon do mongoDB : sudo service mongod start <br />
        - No diretório do projeto executat "pip install -r requirements.pip" (isso resolverá as dependencias para o python) <br />
        - Rodar a api : python api.py <br />
Utilização
==========
### Inserção de um novo mapa de malha logistica.

 Ex.: POST http//localhost:5000/maps

    Content:
    ```
    {
        "title":"testemaps",
        "routes":[
            {
                "origin":"A",
                "destiny":"B",
                "distance":10
            },
            {
                "origin":"B",
                "destiny":"D",
                "distance":15
            },
            {
                "origin":"A",
                "destiny":"C",
                "distance":20
            },
            {
                "origin":"C",
                "destiny":"D",
                "distance":30
            },
            {
                "origin":"B",
                "destiny":"E",
                "distance":50
            },
            {
                "origin":"D",
                "destiny":"E",
                "distance":30
            }
        ]
    }
    ```

    Descrição dos campos:
        - origin : string
        - destiny : string
        - distance : float

  Retornos:
  - <u> Http Response 201 (Created) :</u><br />
        - A malha foi criada com sucesso.
  - <u> JSON return: </u><br />
    ``` 
         {
          "_updated": "Thu, 17 Mar 2016 03:13:58 GMT",
          "_links": {
            "self": {
              "href": "maps/56ea20f6e1382324a7744c59",
              "title": "Map"
            }
          },
          "_created": "Thu, 17 Mar 2016 03:13:58 GMT",
          "_status": "OK",
          "_id": "56ea20f6e1382324a7744c59",
          "_etag": "25a2714cd56af423e7e9ee0d42a52ae9935f7efa"
        }
    ```
        
  - <u> Http Response 400 (Bad request) :</u> <br />
        - Algum campo não passou na validação, podendo estar vazio, o json enviado não segue o padrão etc.
  - <u>JSON return: </u><br />
    ```
        {

          "_status": "ERR",
          "_error": {
            "message": "The browser (or proxy) sent a request that this server could not understand.",
            "code": 400
          }

        }
    ```
  - <u>Http Response 422 (Unprocessable Entity) :</u> <br />
        - Algum campo não segue o tipo pré determinado à ele, campo será informado no retorno.
  - <u>JSON return:</u> <br />
    ```
        {

          "_status": "ERR",
          "_issues": {
            "routes": {
              "1": {
                "destiny": "must be of string type"
              }
            }
          },
          "_error": {
            "message": "Insertion failure: 1 document(s) contain(s) error(s)",
            "code": 422
          }

        }
    ```
  - <u>Http Response 500 (Internal Server Error) :</u> <br />
        - Problema de comunicação entre as partes internas da aplicação.
  - <u>HTML return: </u><br />
    ```
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>500 Internal Server Error</title>
        <h1>Internal Server Error</h1>
        <p>The server encountered an internal error and was unable to complete your request.  Either the server is overloaded or there is an error in the application.</p>
    ```
### Requisitar o melhor caminho (shortest path)
  
 Ex.: GET http://localhost:5000/maps/shortest?map=mapaPrincipal&origin=A&destiny=D&price=2.50&autonomy=10
 
    Content:
    ```
        {

          "data": [
            {
              "Path": "['A', 'B', 'D']"
            },
            {
              "Total KM": "25.00"
            },
            {
              "Cost": "6.25"
            }
          ]

        }
    ```
  - <u>Http Response 400 (Bad Request) :</u> <br />
        - Algum dos parâmetros passados é inválido. Ele será informado no retorno json.
  - <u>Json return :</u> <br />
    ```
        {
          "response": "The parameter destiny does not contain on map mapaPrincipal"
        }
    ```

   - <u>Http Response 500 (Internal Server Error) :></u> <br />
        - Problema de comunicação entre as partes internas da aplicação.
        
   - <u>Json return :</u> <br />
    ```
        {
          "response": "Application could not use the DB especifield"
        }
    ```

### Requisitar todos maps existentes.

 Ex.: GET http://localhost:5000/maps

    Content:
    {
      "_items": [
        {
          "_updated": "Thu, 17 Mar 2016 03:38:46 GMT",
          "title": "testemaps3",
          "_links": {
            "self": {
              "href": "maps/56ea26c6e138232ef1ae4f62",
              "title": "Map"
            }
          },
          "routes": [
            {
              "origin": "A",
              "distance": 10,
              "destiny": "C"
            },
            {
              "origin": "B",
              "distance": 20,
              "destiny": "D"
            }
          ],
          "_created": "Thu, 17 Mar 2016 03:38:46 GMT",
          "_id": "56ea26c6e138232ef1ae4f62",
          "_etag": "93b22140322485aee19c5cabcb9d9957fe441ab6"
        },
        {
          "_updated": "Thu, 17 Mar 2016 03:39:01 GMT",
          "title": "testemaps1",
          "_links": {
            "self": {
              "href": "maps/56ea26d5e138232ef1ae4f63",
              "title": "Map"
            }
          },
          "routes": [
            {
              "origin": "A",
              "distance": 5,
              "destiny": "C"
            },
            {
              "origin": "B",
              "distance": 20,
              "destiny": "F"
            }
          ],
          "_created": "Thu, 17 Mar 2016 03:39:01 GMT",
          "_id": "56ea26d5e138232ef1ae4f63",
          "_etag": "c89227a0d84f96525361c5a9bd0404689a7a1b50"
        }
      ],
      "_links": {
        "self": {
          "href": "maps",
          "title": "maps"
        },
        "parent": {
          "href": "/",
          "title": "home"
        }
      },
      "_meta": {
        "max_results": 25,
        "total": 2,
        "page": 1
      }
    }

### Requisitar um mapa especifico.

 Ex.: GET http://localhost:5000/maps/56ea26d5e138232ef1ae4f63 ou http://localhost:5000/maps/testemaps1

    Content:
        {
          "_updated": "Thu, 17 Mar 2016 03:39:01 GMT",
          "title": "testemaps1",
          "_links": {
            "self": {
              "href": "maps/56ea26d5e138232ef1ae4f63",
              "title": "Map"
            },
            "collection": {
              "href": "maps",
              "title": "maps"
            },
            "parent": {
              "href": "/",
              "title": "home"
            }
          },
          "routes": [
            {
              "origin": "A",
              "distance": 5,
              "destiny": "C"
            },
            {
              "origin": "B",
              "distance": 20,
              "destiny": "F"
            }
          ],
          "_created": "Thu, 17 Mar 2016 03:39:01 GMT",
          "_id": "56ea26d5e138232ef1ae4f63",
          "_etag": "c89227a0d84f96525361c5a9bd0404689a7a1b50"
        }

  - <u>Http Response 200 (OK) :</u> <br />
        - Retornou o mapa com sucesso.
  - <u>JSON return :</u> <br />
        - O conteudo do mapa mais alguns parametros para controle da api. (Ex acima)
    
  - <u>Http Response 404 (Not Found):</u> <br />
        - Não foi encontrado o mapa requisitado. O id é inválido ou existe algo errado na URL.
  - <u>JSON return :</u> <br />
    ```
        {
          "_status": "ERR",
          "_error": {
            "message": "The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.",
            "code": 404
          }
        }
    ```
    
  - <u>Http Response 500 (Internal Server Error) :</u> <br />
        - Problema de comunicação entre as partes internas da aplicação.
  - <u>HTML return :</u> <br />
    ```
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>500 Internal Server Error</title>
        <h1>Internal Server Error</h1>
        <p>The server encountered an internal error and was unable to complete your request.  Either the server is overloaded or there is an error in the application.</p>
    ```

Motivação para o uso das tecnologias:
====================================
  - <u>MongoDB :</u> <br />
        O mongoDb além de facilitar todo o armazenamento dos dados nesse tipo de aplicação, também, é utilizado pelo EVE que também foi utilizado aqui nessa aplicação. 
        Também cogitei usar o Neo4J que é um banco de dados especializado em grafos e facilitaria os calculos das malhas de rotas, porém, não tenho tanto conhecimento nessa tecnologia e foi escolhido manter a maior estabilidade.
  - <u>EVE :</u> <br />
        O microFramework eve constroi por si só toda a estrutura dos responses da API apenas em base do modelo que é definido para o banco de dados mongoDb. Além de controlar os IDs e definir links de acesso para cada item inserido. Assim facilitando para receber um documento Json e armazenar em minha collection de forma simples e descomplicada.
  - <u>Dijkstra :</u> <br />
	Fiz uso do algoritmo de dijkstra para poder calcular o menor caminho entre dois vertices, após alguns teste e pesquisas acabei seguindo como base, principalmente, dois artigos : 
	http://interactivepython.org/runestone/static/pythonds/Graphs/DijkstrasAlgorithm.html
	http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
	Então fica aqui meus créditos aos autores.
	


