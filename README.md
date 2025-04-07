# poes-library-back
## Endpoints 
### Author
* get/post: api/v1/authors/
  * payload:
      ```
        {
          "is_active": true,
          "name": "João",
          "about": "Escritor.",
          "birth": "2002-01-25",
          "birthplace": "Teresina, Piauí, BR",
          "death": "2082-10-07",
          "place_of_death": "Teresina"
        }
      ```
* retrieve/update/patch/delete: api/v1/authors/id
    * payload:
        ```
          {
            "id": 1,
            "is_active": true,
            "name": "George Orwell",
            "about": "Eric Arthur Blair, mais conhecido pelo pseudónimo George Orwell, foi um escritor, ensaísta político inglês, nascido na Índia Britânica.",
            "birth": "1903-06-25",
            "birthplace": "Motihari, Índia",
            "death": "1950-01-21",
            "place_of_death": "University College Hospital, Londres, Reino Unido"
          }
        ```

### Book
* get/post: api/v1/books/
  * payload:
      ```
        {
          "is_active": false,
          "name": "Comédia"
        }
      ```
* retrieve/update/patch/delete: /api/v1/books/id
    * payload:
        ```
          {
            "id": 1,
            "is_active": false,
            "name": "Ficção"
          }
        ```

### Genre
* get/post: api/v1/genres/
  * payload:
      ```
        {
          "author": [
            {
              "name": "Edgar Allan Poe"
            }
          ],
          "genre": {
            "name": "Horror"
          },
          "is_active": true,
          "title": "O gato preto",
          "synopsis": "Poe conta a história de um homem que, movido pelo abuso de álcool e transtornado pelo amor incondicional que um bicho pode dedicar a seu dono, acaba por enforcar seu próprio gato de estimação. Perseguido pelo fantasma do gato, ele adota outro animal, que, com o passar do tempo, além de despertar a mesma aversão em seu dono, revela, em sua pelagem, a marca da forca.",
          "about": "O Gato Preto em inglês: The Black Cat é um conto do escritor estadunidense Edgar Allan Poe. Foi publicado em uma edição do Saturday Evening Post de 19 de agosto de 1843. É um estudo da psicologia da culpa, também comparado ao conto \"The Tell-Tale Hea",
          "publication": "1843-08-19"
        }
      ```
* retrieve/update/patch/delete: api/v1/genres/id
    * payload:
        ```
          {
            "author": [
            {
              "name": "Edgar Allan Poe"
            }
          ],
          "genre": {
            "name": "Horror"
          },
          "is_active": true,
          "title": "O gato preto",
          "synopsis": "Poe conta a história de um homem que, movido pelo abuso de álcool e transtornado pelo amor incondicional que um bicho pode dedicar a seu dono, acaba por enforcar seu próprio gato de estimação. Perseguido pelo fantasma do gato, ele adota outro animal, que, com o passar do tempo, além de despertar a mesma aversão em seu dono, revela, em sua pelagem, a marca da forca.",
          "about": "O Gato Preto em inglês: The Black Cat é um conto do escritor estadunidense Edgar Allan Poe. Foi publicado em uma edição do Saturday Evening Post de 19 de agosto de 1843. É um estudo da psicologia da culpa, também comparado ao conto \"The Tell-Tale Hea",
          "publication": "1843-08-19"
          }
        ```
* query patameters:
  * ?title={titulo}
  * ?author={id ou nome}
  * ?publication{aaa/mm/dd}