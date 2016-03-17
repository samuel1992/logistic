LogisticRoute
=============

Descrição
=========
Sistema para calcular uma malha logística. Basicamente o sistema deve ser capaz de receber duas rotas (ponto de partida e de chegada) e a partir dessas informações calcular qual seria a melhor rota em termos de custo (gasolina por KM percorrido).
Uma malha logística segue o seguinte formato :<br /> 

A B 10
B D 15
A C 20
C D 30
B E 50
D E 30

Onde a primeira coluna é o ponto de partida, a segunda o pontode chegada e a terceira representa o total de KM entre um e outro.

Instalação
==========
  - Pré-requsitos:<br />
        - MongoDB
        - Eve
		- PyMongo
        - Python 2.7

Utilização
==========
### Inserção de um novo mapa de malha logistica.

 Ex.:<br /> POST http//localhost:5000/maps

    Content:<br />
    <code>
    {
        "title":<br />"testemaps",
        "routes":<br />[
            {
                "origin":<br />"A",
                "destiny":<br />"B",
                "distance":<br />10
            },
            {
                "origin":<br />"B",
                "destiny":<br />"D",
                "distance":<br />15
            },
            {
                "origin":<br />"A",
                "destiny":<br />"C",
                "distance":<br />20
            },
            {
                "origin":<br />"C",
                "destiny":<br />"D",
                "distance":<br />30
            },
            {
                "origin":<br />"B",
                "destiny":<br />"E",
                "distance":<br />50
            },
            {
                "origin":<br />"D",
                "destiny":<br />"E",
                "distance":<br />30
            }
        ]
    }
    </code>

    Descrição dos campos:<br />
        - origin :<br /> string
        - destiny :<br /> string
        - distance :<br /> float

  Retornos:<br />
  - Http Response 201 (Created) :<br />
        - A malha foi criada com sucesso.
  - JSON return:<br />
         {
          "_updated":<br /> "Thu, 17 Mar 2016 03:13:58 GMT",
          "_links":<br /> {
            "self":<br /> {
              "href":<br /> "maps/56ea20f6e1382324a7744c59",
              "title":<br /> "Map"
            }
          },
          "_created":<br /> "Thu, 17 Mar 2016 03:13:58 GMT",
          "_status":<br /> "OK",
          "_id":<br /> "56ea20f6e1382324a7744c59",
          "_etag":<br /> "25a2714cd56af423e7e9ee0d42a52ae9935f7efa"
        }
        
  - Http Response 400 (Bad request) :<br />
        - Algum campo não passou na validação, podendo estar vazio, o json enviado não segue o padrão.
  - JSON return:<br />
        {
          "_status":<br /> "ERR",
          "_error":<br /> {
            "message":<br /> "The browser (or proxy) sent a request that this server could not understand.",
            "code":<br /> 400
          }
        }
  - Http Response 422 (Unprocessable Entity) :<br />
        - Algum campo não segue o tipo pré determinado à ele, campo será informado no retorno.
  - JSON return:<br />
        {
          "_status":<br /> "ERR",
          "_issues":<br /> {
            "routes":<br /> {
              "1":<br /> {
                "destiny":<br /> "must be of string type"
              }
            }
          },
          "_error":<br /> {
            "message":<br /> "Insertion failure: 1 document(s) contain(s) error(s)",
            "code":<br /> 422
          }
        }
  - Http Response 500 (Internal Server Error) :<br /> 
        - Problema de comunicação entre as partes internas da aplicação.
  - HTML return:<br />
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>500 Internal Server Error</title>
        <h1>Internal Server Error</h1>
        <p>The server encountered an internal error and was unable to complete your request.  Either the server is overloaded or there is an error in the application.</p>

### Requisitar todos maps existentes.

 Ex.:<br /> GET http://localhost:5000/maps

    Content:<br />
    {
      "_items":<br /> [
        {
          "_updated":<br /> "Thu, 17 Mar 2016 03:38:46 GMT",
          "title":<br /> "testemaps3",
          "_links":<br /> {
            "self":<br /> {
              "href":<br /> "maps/56ea26c6e138232ef1ae4f62",
              "title":<br /> "Map"
            }
          },
          "routes":<br /> [
            {
              "origin":<br /> "A",
              "distance":<br /> 10,
              "destiny":<br /> "C"
            },
            {
              "origin":<br /> "B",
              "distance":<br /> 20,
              "destiny":<br /> "D"
            }
          ],
          "_created":<br /> "Thu, 17 Mar 2016 03:38:46 GMT",
          "_id":<br /> "56ea26c6e138232ef1ae4f62",
          "_etag":<br /> "93b22140322485aee19c5cabcb9d9957fe441ab6"
        },
        {
          "_updated":<br /> "Thu, 17 Mar 2016 03:39:01 GMT",
          "title":<br /> "testemaps1",
          "_links":<br /> {
            "self":<br /> {
              "href":<br /> "maps/56ea26d5e138232ef1ae4f63",
              "title":<br /> "Map"
            }
          },
          "routes":<br /> [
            {
              "origin":<br /> "A",
              "distance":<br /> 5,
              "destiny":<br /> "C"
            },
            {
              "origin":<br /> "B",
              "distance":<br /> 20,
              "destiny":<br /> "F"
            }
          ],
          "_created":<br /> "Thu, 17 Mar 2016 03:39:01 GMT",
          "_id":<br /> "56ea26d5e138232ef1ae4f63",
          "_etag":<br /> "c89227a0d84f96525361c5a9bd0404689a7a1b50"
        }
      ],
      "_links":<br /> {
        "self":<br /> {
          "href":<br /> "maps",
          "title":<br /> "maps"
        },
        "parent":<br /> {
          "href":<br /> "/",
          "title":<br /> "home"
        }
      },
      "_meta":<br /> {
        "max_results":<br /> 25,
        "total":<br /> 2,
        "page":<br /> 1
      }
    }

### Requisitar um mapa especifico.

 Ex.:<br /> GET http://localhost:5000/maps/56ea26d5e138232ef1ae4f63 ou http://localhost:5000/maps/testemaps1

    Content:<br />
        {
          "_updated":<br /> "Thu, 17 Mar 2016 03:39:01 GMT",
          "title":<br /> "testemaps1",
          "_links":<br /> {
            "self":<br /> {
              "href":<br /> "maps/56ea26d5e138232ef1ae4f63",
              "title":<br /> "Map"
            },
            "collection":<br /> {
              "href":<br /> "maps",
              "title":<br /> "maps"
            },
            "parent":<br /> {
              "href":<br /> "/",
              "title":<br /> "home"
            }
          },
          "routes":<br /> [
            {
              "origin":<br /> "A",
              "distance":<br /> 5,
              "destiny":<br /> "C"
            },
            {
              "origin":<br /> "B",
              "distance":<br /> 20,
              "destiny":<br /> "F"
            }
          ],
          "_created":<br /> "Thu, 17 Mar 2016 03:39:01 GMT",
          "_id":<br /> "56ea26d5e138232ef1ae4f63",
          "_etag":<br /> "c89227a0d84f96525361c5a9bd0404689a7a1b50"
        }

  - Http Response 200 (OK) :<br />
        - Retornou o mapa com sucesso.
  - JSON return:<br />
        - O conteudo do mapa mais alguns parametros para controle da api. (Ex acima)
    
  - Http Response 404 (Not Found):<br />
        - Não foi encontrado o mapa requisitado. O id é inválido ou existe algo errado na URL.
  - JSON return:<br />
        {
          "_status":<br /> "ERR",
          "_error":<br /> {
            "message":<br /> "The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.",
            "code":<br /> 404
          }
        }
    
  - Http Response 500 (Internal Server Error) :<br />
        - Problema de comunicação entre as partes internas da aplicação.
  - HTML return:<br />
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>500 Internal Server Error</title>
        <h1>Internal Server Error</h1>
        <p>The server encountered an internal error and was unable to complete your request.  Either the server is overloaded or there is an error in the application.</p>

Motivação para o uso das tecnologias:<br />
====================================
  - MongoDB :<br />
        O mongoDb além de facilitar todo o armazenamento dos dados nesse tipo de aplicação, também, é utilizado pelo EVE que também foi utilizado aqui nessa aplicação. 
        Também cogitei usar o Neo4J que é um banco de dados especializado em grafos e facilitaria os calculos das malhas de rotas, porém, não tenho tanto conhecimento nessa tecnologia e foi escolhido manter a maior estabilidade.
  - EVE :<br />
        O microFramework eve constroi por si só toda a estrutura dos responses da API apenas em base do modelo que é definido para o banco de dados mongoDb. Além de controlar os IDs e definir links de acesso para cada item inserido.

        
        
            
    
        
    
        
        

    
