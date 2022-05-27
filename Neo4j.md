#https://sandbox.neo4j.com/login
#? QUE ES NEO4J?
# Neo4j is the world’s leading graph database. The architecture is designed for optimal management, storage, 
# and traversal of nodes and relationships. The graph database takes a property graph approach, which is beneficial 
# for both traversal performance and operations runtime.


#? CYPHER: LENGUAJE DE NEO4J
# Cypher is Neo4j’s graph query language that allows users to store and retrieve data from the graph database. 
# It is a declarative, SQL-inspired language for describing visual patterns in graphs using ASCII-art syntax. 
# The syntax provides a visual and logical way to match patterns of nodes and relationships in the graph. 
# Cypher has been designed to be easy to learn, understand, and use for everyone, 
# but also incorporate the power and functionality of other standard data access languages.


#?### ESTRUCTURA DE GRAFOS DE NEO4J
# Neo4j uses a property graph database model.
# A graph data structure consists of nodes (discrete objects) that can be connected by relationships.
#? The Neo4j property graph database model consists of:

# Nodes describe entities (discrete objects) of a domain
# Nodes can have zero or more labels to define (classify) what kind of nodes they are.
# Relationships describes a connection between a source node and a target node.
#! Relationships always has a direction (one direction).
#! Relationships must have a type (one type) to define (classify) what type of relationship they are.
# Nodes and relationships can have properties (key-value pairs), which further describe them.



#EJEMPLO
#CREATE (:Person:Actor {name: 'Tom Hanks', born: 1956})-[:ACTED_IN {roles: ['Forrest']}]
# ->(:Movie {title: 'Forrest Gump'})<-[:DIRECTED]-(:Person {name: 'Robert Zemeckis', born: 1951})

## ((NODE-ACTOR : NAME TOM HANKS, AGER 57)) >>> acted in >>> ((NODE-MOVIE)) >>> directed by >>> ((NODE-DIRECTOR))




#?### NODOS
#Nodes are used to represent entities (discrete objects) of a domain.
#The simplest possible graph is a single node with no relationships. Consider the following graph, consisting of a single node.

#The node labels are:
#Person
#Actor
#The properties are:
#name: Tom Hanks
#born: 1956
#? The node can be created with Cypher using the query:  CREATE (:Person:Actor {name: 'Tom Hanks', born: 1956})


#?### NODE LABELS
#Labels shape the domain by grouping (classifying) nodes into sets where all nodes with a certain label belong to the same set.
#For example, all nodes representing users could be labeled with the label User. With that in place, 
# you can ask Neo4j to perform operations only on your user nodes, such as finding all users with a given name.
#Since labels can be added and removed during runtime, they can also be used to mark temporary states for nodes.
# A Suspended label could be used to denote bank accounts that are suspended, and a Seasonal label can denote vegetables 
# that are currently in season.
#A node can have zero to many labels
#In the example graph, the node labels, Person, Actor, and Movie, are used to describe (classify) the nodes. 
# More labels can be added to express different dimensions of the data.
#The following graph shows the use of multiple labels.


#?### RELACIONES
#A relationship describes how a connection between a source node and a target node are related. 
# It is possible for a node to have a relationship to itself.

#A relationship:
# Connects a source node and a target node.
# Has a direction (one direction).
# Must have a type (one type) to define (classify) what type of relationship it is.
# Can have properties (key-value pairs), which further describe the relationship.
# Relationships organize nodes into structures, allowing a graph to resemble a list, a tree, a map, 
# or a compound entity — any of which may be combined into yet more complex, richly inter-connected structures.


'''
The relationship type: ACTED_IN

The properties are:

roles: ['Forrest']

performance: 5

The roles property has an array value with a single item ('Forrest') in it.

The relationship can be created with Cypher using the query:

CREATE ()-[:ACTED_IN {roles: ['Forrest'], performance: 5}]->()
'''
###
'''
Relationships always have a direction. However, the direction can be disregarded where it is not useful. This means that there is no need to add duplicate relationships in the opposite direction unless it is needed to describe the data model properly.

A node can have relationships to itself. To express that Tom Hanks KNOWS himself
'''

#?>###PROPIEDADES

#The value part of a property:
#Can hold different data types, such as number, string, or boolean.
#Can hold a homogeneous list (array) containing, for example, strings, numbers, or boolean values

#CREATE (:Example {a: 1, b: 3.14})
#The property a has the type integer with the value 1.
#The property b has the type float with the value 3.14.


#CREATE (:Example {f: [1, 2, 3], g: [2.71, 3.14], h: ['abc', 'example'], i: [true, true, false]})
#The property f contains an array with the value [1, 2, 3].
#The property g contains an array with the value [2.71, 3.14].
#The property h contains an array with the value ['abc', 'example'].
#The property i contains an array with the value [true, true, false].


#?### Traversals and paths
#traversal is how you query a graph in order to find answers to questions, for example: "What music do my friends like that I don’t yet own?",
# or "What web services are affected if this power supply goes down?".
#Traversing a graph means visiting nodes by following relationships according to some rules. 
# In most cases only a subset of the graph is visited.


#To find out which movies Tom Hanks acted in according to the tiny example database, 
# the traversal would start from the Tom Hanks node, follow any ACTED_IN relationships connected to the node, 
# and end up with Forrest Gump as the result (see the dashed lines):

#! A path containing only a single node has the length of 0
#! A path containing one relationship has the length of 1.

#?### ESQUEMA
# Neo4j is often described as schema optional, meaning that it is not necessary to create indexes and constraints. 
# You can create data — nodes, relationships and properties — without defining a schema up front.
# Indexes and constraints can be introduced when desired, in order to gain performance or modeling benefits.




#?### INDICES
#Indexes are used to increase performance. 

#?### RESTRICICONES
#Constraints are used to make sure that the data adheres to the rules of the domain.


#?### RELACIONES EN LOS GRAFOS
#By assembling nodes and relationships into connected structures, 
# graph databases enable us to build simple and sophisticated models that map closely to our problem domain. 
# The data stays remarkably similiar to its form in the real world - small, normalized, yet richly connected entities. 
# This allows you to query and view your data from any imaginable point of interest, supporting many different use cases.

#Each node (entity or attribute) in the graph database model directly and physically contains a list of relationship 
# records that represent the relationships to other nodes. These relationship records are organized by type and direction
# and may hold additional attributes. Whenever you run the equivalent of a JOIN operation, the graph database uses this list,
# directly accessing the connected nodes and eliminating the need for expensive search-and-match computations.


#USO DEL SOFWARE
# https://youtu.be/hIvNexwVYNw



# cypher 
# Cypher is a declarative graph query language that allows for expressive and efficient querying,
# updating and administering of the graph. It is designed to be suitable for both developers and operations professionals. 
# Cypher is designed to be simple, yet powerful; highly complicated database queries can be easily expressed, 
# enabling you to focus on your domain, instead of getting lost in database access.


#Cypher is inspired by a number of different approaches and builds on established practices for expressive querying.
# Many of the keywords, such as WHERE and ORDER BY, are inspired by SQL. P
# Cypher borrows its structure from SQL — queries are built up using various clauses.
# The following are a few examples of clauses used to read from the graph:
#?MATCH: The graph pattern to match. This is the most common way to get data from the graph.
#! similar a un join 
#?WHERE: Not a clause in its own right, but rather part of MATCH, OPTIONAL MATCH and WITH. Adds constraints to a pattern, or filters the intermediate result passing through WITH.
#?RETURN: What to return.

'''
MATCH (user)-[:FRIEND]->(follower)
WHERE user.name IN ['Joe', 'John', 'Sara', 'Maria', 'Steve'] AND follower.name =~ 'S.*'
RETURN user.name, follower.name

'''

#?CREATE (and DELETE): Create (and delete) nodes and relationships.
#?SET (and REMOVE): Set values to properties and add labels on nodes using SET and use REMOVE to remove them.
#?MERGE: Match existing or create new nodes and patterns. This is especially useful together with unique constraints.

###############################################################################################################################
##########propiedades de los grafos

'''
Gráfico de propiedades
En el módulo anterior nos referimos a los nodos y las relaciones como los bloques de construcción fundamentales para un gráfico. En esta lección aprenderá sobre los elementos adicionales que Neo4j admite para hacer un gráfico de propiedades.

Nodos, etiquetas y propiedades
Recordemos que los nodos son los elementos gráficos que representan las cosas en nuestros datos. Podemos usar dos elementos adicionales para proporcionar un contexto adicional a los datos.

Echemos un vistazo a cómo podemos usar estos elementos adicionales para mejorar nuestro gráfico social.

Etiquetas
Nodos con etiquetas
Al agregar una etiqueta a un nodo, estamos significando que el nodo pertenece a un subconjunto de nodos dentro del gráfico. Las etiquetas son importantes en Neo4j porque proporcionan un punto de partida para una consulta de Cypher.

Tomemos a Michael y Sarah: en este contexto, ambos nodos son personas.

Podemos embellecer el gráfico añadiendo más etiquetas a estos nodos; Michael se identifica como hombre y Sarah es mujer. En este contexto, Michael es un empleado de una empresa, pero no tenemos ninguna información sobre el estado laboral de Sarah.

Michael trabaja para una compañía llamada Graph Inc, por lo que podemos agregar esa etiqueta al nodo que representa a una empresa.

En Neo4j, un nodo puede tener cero, una o varias etiquetas.
Propiedades del nodo
Hasta ahora estamos asumiendo que los nodos representan a Michael, Sarah y Graph Inc. Podemos hacer este concreto agregando propiedades al nodo.

Las propiedades son pares de claves, valores y se pueden agregar o quitar de un nodo según sea necesario. Los valores de propiedad pueden ser un único valor o una lista de valores que se ajustan al sistema de tipos Cypher.

Nodos con propiedades
Al agregar las propiedades firstName y lastName, podemos ver que el nodo Michael se refiere a Michael Faraday, conocido por la ley de inducción de Faraday, la jaula de Faraday y menos conocido como el inventor del Globo de Fiesta. Miguel nació el 22 de septiembre de 1791.

El nombre completo de Sarah es Sarah Faraday, y su apellido de soltera es Barnard.

Al observar la propiedad del nombre en el nodo Graph Inc, podemos ver que se refiere a la compañía Graph Inc, con una ciudad de Londres, tiene 56 empleados (numEmployees), y hace negocios como Graph Incorporated y GI (dba).

No es necesario que existan propiedades para cada nodo con una etiqueta en particular. Si una propiedad no existe para un nodo, se trata como un valor.null
Relaciones
Una relación en Neo4j es una conexión entre dos nodos.

Dirección de la relación
Relaciones con la dirección
En Neo4j, cada relación debe tener una dirección en el gráfico. Aunque se requiere esta dirección, la relación se puede consultar en cualquier dirección o ignorarse por completo en el momento de la consulta.

Se crea una relación entre un nodo de origen y un nodo de destino, por lo que estos nodos deben existir antes de crear la relación.

Si consideramos el concepto de gráficos dirigidos y no dirigidos que discutimos en el módulo anterior, la dirección de la relación MARRIED_TO debe existir y puede proporcionar algún contexto adicional, pero puede ignorarse para el propósito de la consulta. En Neo4j, la relación MARRIED_TO debe tener una dirección.

La dirección de una relación puede ser importante cuando se trata de jerarquía, aunque si las relaciones apuntan hacia arriba o hacia abajo hacia el árbol es una decisión arbitraria.

Tipo de relación
Relaciones con tipos
Cada relación en un grafo neo4j debe tener un tipo. Esto nos permite elegir en el momento de la consulta qué parte del gráfico recorreremos.

Por ejemplo, podemos atravesar cada relación de Michael, o podemos especificar la MARRIED_TO relación termine solo en el nodo de Sarah.

Aquí hay ejemplos de instrucciones de consulta de Cypher para admitir esto:

cifrar
// traverse the Michael node to return the Sarah node
MATCH (p:Person {firstName: 'Michael'})-[:MARRIED_TO]-(n) RETURN n;

// traverse the Michael node to return the Graph Inc node
MATCH (p:Person {firstName: 'Michael'})-[:WORKS_AT]-(n) RETURN n;

// traverse all relationships from the Michael node
// to return the Sarah node and the Graph Inc node
MATCH (p:Person {firstName: 'Michael'})--(n) RETURN n
Propiedades de la relación
Al igual que con los nodos, las relaciones también pueden tener propiedades. Estos pueden referirse a un costo o distancia en un gráfico ponderado o simplemente proporcionar contexto adicional a una relación.

Relaciones con propiedades
En nuestro gráfico, podemos colocar una propiedad en la relación MARRIED_TO para mantener la fecha en que Michael y Sarah se casaron. Esta relación WORKS_AT tiene una propiedad de roles para significar cualquier rol que el empleado haya ocupado en la empresa. Si Michael también trabajara en otra compañía, su relación WORKS_AT con la otra compañía tendría un valor diferente para la propiedad de los roles.
'''



######################################################################################################################3333

#VENTAJAS DE CYPHER
'''
Neo4j es una base de datos de gráficos nativa
Neo4j es una base de datos de gráficos nativa, lo que significa que todo, desde el almacenamiento de los datos hasta el lenguaje de consulta, se ha diseñado específicamente teniendo en cuenta el recorrido.

Donde las bases de datos de gráficos nativos se distinguen de otras bases de datos es el concepto de adyacencia sin índices. Cuando se confirma una transacción de base de datos, se almacena una referencia a la relación con los nodos tanto al principio como al final de la relación. Como cada nodo es consciente de cada relación entrante y saliente conectada a él, el motor de gráficos subyacente simplemente perseguirá punteros en la memoria, algo en lo que las computadoras son excepcionalmente buenas.

Adyacencia sin índices (IFA)
Una de las características clave que hace que las bases de datos de gráficos Neo4j sean diferentes de un RDBMS es que Neo4j implementa la adyacencia sin índices.

Consulta RDBMS
Tabla relacional1
Para comprender mejor el beneficio de la adyacencia sin índices, veamos cómo se ejecuta una consulta en un RDBMS.

Supongamos que tiene esta tabla en el RDBMS.

Ejecute esta consulta SQL para encontrar los padres de tercer grado del grupo con el identificador de 3:

SQL
SELECT PARENT_ID
FROM GROUPS
WHERE ID = (SELECT PARENT_ID
    FROM GROUPS
    WHERE ID = (SELECT PARENT_ID
        FROM GROUPS
        WHERE ID = 3))
El resultado de esta consulta es 1, pero para determinar este resultado, SQL Server necesitaba:

Localice la cláusula más interna.

Cree el plan de consulta para la subcláusula.

Ejecute el plan de consulta para la subcláusula.

Busque la siguiente cláusula más interna.

Repita los pasos 2 a 4.

Resultando en:

3 ciclos de planificación

3 búsquedas de índice

3 lecturas de base de datos

Almacenamiento Neo4j
Con la adyacencia sin índices, Neo4j almacena nodos y relaciones como objetos que están vinculados entre sí a través de punteros. Conceptualmente, el gráfico se ve así:

IFA-1-nuevo
Estos nodos y relaciones se almacenan como:

IFA-2-nuevo
Consulta Neo4j Cypher
Supongamos que tuviéramos esta consulta en Cypher:

Cifrar
MATCH (n) <-- (:Group) <-- (:Group) <-- (:Group {id: 3})
RETURN n.id
Usando IFA, el motor de gráficos Neo4j comienza con el anclaje de la consulta, que es el nodo Grupo con el identificador de 3. A continuación, utiliza los enlaces almacenados en la relación y los objetos de nodo para atravesar el patrón de gráfico.

IFA-3-nuevo
Para realizar esta consulta, el motor de gráficos Neo4j necesitaba:

Planifique la consulta en función del anclaje especificado.

Utilice un índice para recuperar el nodo de anclaje.

Siga los punteros para recuperar el nodo de resultado deseado.

Los beneficios de IFA en comparación con el acceso relacional a DBMS son:

Menos búsquedas de índices.

Sin escaneos de tablas.

Reducción de la duplicación de datos.
'''
## ##############################################################################################
>>  El gráfico de la película
A lo largo de los cursos de GraphAcademy, utilizará alguna versión de la base de datos de películas para adquirir experiencia con Neo4j. En esta lección, aprenderá sobre los datos en la base de datos de películas "starter" que se utiliza cuando está aprendiendo Cypher por primera vez.

Nodos
Los nodos de la base de datos movie representan personas, películas y, en algunas versiones de la base de datos Movie, géneros para las películas.

Nodos de la base de datos de películas
La versión "starter" de la base de datos Movie contiene 171 nodos:

38 Nodos de película (nodos con la etiqueta Película)

133 nodos persona (nodos con la etiqueta Persona)

Esta es la base de datos que utiliza para aprender primero Cypher.

Propiedades del nodo
Propiedades de los nodos de película
Todos los nodos De película tienen una propiedad, título que se utiliza para identificar de forma exclusiva una película. Esta propiedad existe para todos los nodos Movie.

Otras propiedades que puede tener un nodo Película son:

lanzado, el año en que se estrenó la película.

eslogan, una frase para describir la película.

Entonces, por ejemplo, vemos en estos dos nodos Movie, ambos tienen un título y una propiedad liberada, pero solo uno de ellos tiene una propiedad de eslogan.

Propiedades de los nodos Persona
Todos los nodos Persona tienen una propiedad, nombre que se utiliza para identificar de forma exclusiva a una persona. Algunos nodos Person tienen una propiedad, nacida, pero no todos.

Relaciones
Como has aprendido, el elemento más importante de una base de datos de gráficos son sus relaciones. Una relación tiene un tipo y una dirección y representa la relación entre dos nodos específicos.

Algunas de las relaciones en el gráfico de la película "starter" incluyen:

Tipo de relación	Descripción	Número en el gráfico
ACTED_IN

Una persona actuó en una película

172

DIRIGIDO

Una persona dirigió una película

44

ESCRIBIÓ

Una persona escribió una película

10

PRODUCIDO

Una persona produjo una película

15

Una persona puede tener múltiples relaciones con una película. Por ejemplo, una persona puede ser tanto un actor como un director para una película en particular. En el gráfico de la película, las personas son actores, directores, escritores y / o productores dadas estas relaciones.

hoffa
Entonces, por ejemplo, la película "Hoffa" en el gráfico de la película tiene estas relaciones. Cuenta con cuatro actores y un director. Danny DeVito dirigió y actuó en esta película. En nuestro gráfico de películas "iniciales", esta película no tiene escritores o productores definidos.

Otras relaciones en el gráfico incluyen:

Relationship type	Description	Number in graph
REVIEWED

A Person reviewed a Movie

9

FOLLOWS

A Person follows another Person

3

Using these relationships, people can be reviewers, followers, or followees. In the Movie graph, people who review movies or follow other people are not actors, directors, writers, or producers.

Here are the reviewers in our "starter" Movie graph:

Algunos críticos de cine
Tenemos tres nodos de persona aquí para las personas que revisaron películas. Los tres críticos revisaron la película, The Replacements. Dos personas aquí están siguiendo a Jessica Thompson.

Propiedades de la relación
La relación ACTED_IN puede tener la propiedad de roles que representa los roles que un actor tenía cuando actuó en una película específica.

Por ejemplo, en la base de datos de películas "starter", el actor, Hugo Weaving, tiene estas propiedades definidas para cada una de sus relaciones ACTED_IN con estas películas:


## ##############################################################################################

Lectura de datos de Neo4j
En este módulo aprenderá a escribir código Cypher para recuperar datos del gráfico.

Aprenderás a:

Recuperar nodos del gráfico.

Recuperar nodos con una etiqueta en particular.

Filtre la recuperación por un valor de propiedad.

Valores de propiedad devueltos.

Recupere nodos y relaciones del gráfico utilizando patrones en el gráfico.

Filtrar consultas

Usando el conjunto de datos de ejemplo De películas, creará y ejecutará código Cypher para encontrar actores y películas en nuestro gráfico.

Modelo de dominio para este curso
Aquí está el modelo de datos utilizado en este curso. El gráfico contiene nodos con las etiquetas Persona y Película. Los nodos de persona tienen varios tipos de relaciones con los nodos de película. Un nodo Persona puede tener una relación FOLLOWS con otro nodo Persona.

# basicamente dos nodos se pueden relacionar de muchas formas 

## ##############################################################################################
¿Qué es Cypher?
Cypher es un lenguaje de consulta diseñado para gráficos.

El modelo de pizarra de nuestras entidades de dominio se almacena en la base de datos como un gráfico. Cuando dibujamos un gráfico en la pizarra, representamos entidades como círculos conectados entre sí mediante flechas. En este ejemplo, las entidades son personas y películas. Tenemos los nodos Persona y Película en nuestro gráfico.

Imagen de pizarra
Al igual que dibujaríamos círculos y flechas en una pizarra, escribimos el patrón en Cypher:

# Los nodos están representados por paréntesis.()

# Usamos dos puntos para significar la(s) etiqueta(s), por ejemplo.(:Person)

# Las relaciones entre nodos se escriben con dos guiones, por ejemplo.(:Person)--(:Movie)

# La dirección de una relación se indica utilizando un símbolo mayor o menor que o , por ejemplo .<>(:Person)-→(:Movie)

# El tipo de relación se escribe entre corchetes entre los dos guiones: y , por ejemplo [][:ACTED_IN]

# Las propiedades dibujadas en una burbuja de voz se especifican en una sintaxis similar a JSON.

# Las propiedades en Neo4j son pares clave/valor, por ejemplo.{name: 'Tom Hanks'}

# Por ejemplo, un patrón de Cypher en el gráfico podría ser:

Parcial
// example Cypher pattern
(m:Movie {title: 'Cloud Atlas'})<-[:ACTED_IN]-(p:Person)
Los dos tipos de nodos en este patrón son Película y Persona. Los nodos Persona tienen una relación de ACTED_IN dirigida con los nodos Película. El nodo Movie específico de este patrón se filtra por la propiedad title con un valor de Cloud Atlas. Así que este patrón representa a todas las personas en el gráfico que actuaron en la película, Cloud Atlas.

Cómo funciona Cypher
Cypher funciona haciendo coincidir patrones en los datos. 
# Recuperamos datos del gráfico usando la palabra clave. Puede pensar que la cláusula es similar a la cláusula FROM de una instrucción SQL.MATCHMATCH

>>> Por ejemplo, si queremos encontrar una Persona en el gráfico, haríamos un patrón de un solo nodo con una etiqueta de - prefijada con dos puntos.MATCH:Person:

Parcial
MATCH (:Person)
// incomplete MATCH clause because we need to return something
Supongamos que queremos recuperar todos los nodos Person del gráfico. Podemos asignar una variable colocando un valor antes de los dos puntos. Usemos la variable . Ahora que representa todos los nodos Person recuperados del gráfico, podemos devolverlos usando la cláusula.ppRETURN

Ejecute este código Cypher:

MATCH (p:Person)
RETURN p
Esta consulta devuelve todos los nodos del gráfico con la etiqueta Person. Puede ver los resultados devueltos mediante la vista de gráfico o la vista de tabla. Al seleccionar la vista de tabla, también puede ver las propiedades de los nodos devueltos.

Ahora, digamos que queremos encontrar el nodo que representa a la persona cuyo nombre es Tom Hanks. Todos nuestros nodos Person tienen una propiedad name. Podemos usar las llaves para especificar el par clave/valor de nombre y Tom Hanks como filtro. Como Tom Hanks es una cuerda, tendremos que colocarla entre comillas simples o dobles.{..}


MATCH (p:Person {name: 'Tom Hanks'})
RETURN p
Esta consulta devuelve un único nodo que representa a Tom Hanks. En la vista gráfica de Neo4j Browser, el nodo se visualiza como una burbuja. También puede ver los resultados devueltos en la vista de tabla, donde puede ver las propiedades del nodo.

En nuestra consulta Cypher, podemos acceder a las propiedades utilizando una notación de puntos. Por ejemplo, para devolver la propiedad name usamos .p.name


MATCH (p:Person {name: 'Tom Hanks'})
RETURN  p.born
Esta consulta devuelve el valor de la propiedad born del nodo Tom Hanks.

# Otra forma de filtrar las consultas es mediante la cláusula, en lugar de especificar el valor de la propiedad en línea con llaves.WHERE


# Esta consulta devuelve los mismos datos que la consulta anterior.

# >>MATCH (p:Person)
# >>WHERE p.name = 'Tom Hanks'
# >>RETURN p.name
# >> A medida que adquiera más experiencia con Cypher, encontrará que el uso para filtrar sus consultas es muy poderoso porque puede agregar más lógica a su cláusula. Aquí hay un ejemplo en el que filtramos por dos valores para el nombre.WHEREWHERE

MATCH (p:Person)
WHERE p.name = 'Tom Hanks' OR p.name = 'Rita Wilson'
RETURN p.name, p.born
Esta consulta devuelve dos nombres y sus años de nacimiento asociados




## ##############################################################################################

Encontrar relaciones
NUESTRO OBJETIVO

Como fanático del cine
# , me gustaría encontrar películas para un actor
# en particular para poder ver una película esta noche.
>> En la lección anterior, usamos la cláusula para encontrar el nodo en nuestra base de datos que representaba a Tom Hanks.MATCH


>> MATCH (p:Person {name: 'Tom Hanks'})
>> RETURN p
Podemos extender el patrón en la cláusula para atravesar todas las relaciones con un tipo de ACTED_IN a cualquier nodo. Nuestro modelo de dominio muestra que la relación ACTED_IN va en una dirección saliente desde el nodo Persona para que podamos agregar la dirección en nuestro patrón. A menudo nos referimos a esto como una travesía.MATCH


# MATCH (p:Person {name: 'Tom Hanks'})-[:ACTED_IN]->()
Nuestro modelo de datos dicta que el nodo en el otro extremo de esa relación será el nodo Movie, por lo que no necesariamente necesitamos especificar la etiqueta :Movie en el nodo, sino que usaremos la variable m.


# MATCH (p:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m)
# RETURN m.title
Este código devuelve los títulos de todos los movimientos en los que Actuó Tom Hanks.

Si nuestro gráfico tuviera diferentes etiquetas, por ejemplo, los nodos Televisión y Película, esta consulta habría devuelto todos los nodos Televisión y Película en los que Actuó Tom Hanks. Es decir, si tuviéramos varios tipos de nodos al final de la ACTED_IN relaciones en nuestro gráfico, podríamos asegurarnos de que solo devolvemos películas.


# MATCH (p:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie)
# RETURN m.title
Dado que nuestro gráfico solo tiene nodos de película que tienen relaciones de ACTED_IN entrantes, esta consulta devuelve exactamente los mismos resultados que la consulta anterior.




# ejercicio 1. cuantos dirigieron la pelicula cloud atlas 
>>> MATCH (m:Movie {title: 'Cloud Atlas'})<-[:DIRECTED]-(P)  RETURN P.name

# ejercicio 2.  en cuantas peliculas actuo emil eifrem 
>>> MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
>>> where p.name = "Emil Eifrem"
>>> 
RETURN  count (m.title)




## ##################################################################################################
Filtrado de consultas
Anteriormente, aprendió que la cláusula se usa para indicar al motor de consultas que filtre qué nodos se recuperan del gráfico. En esta lección aprenderá sobre algunas de las formas en que puede filtrar sus consultas.WHERE

Ya ha aprendido cómo puede probar la igualdad para las propiedades de un nodo y cómo puede usar expresiones lógicas para filtrar aún más lo que desea recuperar.

Por ejemplo, esta consulta recupera los nodos Persona y Película donde la persona actuó en una película que se lanzó en 2008 o 2009:
# MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
# WHERE m.released = 2008 OR m.released = 2009
# RETURN p, m


Filtrado por etiquetas de nodo
Ya has visto este tipo de consulta. Devuelve los nombres de todas las personas que actuaron en la película, The Matrix.
# MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
# WHERE m.title='The Matrix'
# RETURN p.name

Una alternativa a esta consulta es la siguiente donde probamos las etiquetas de nodo en la cláusula:WHERE
# MATCH (p)-[:ACTED_IN]->(m)
# WHERE p:Person AND m:Movie AND m.title='The Matrix'
# +RETURN p.name
Ambas consultas se ejecutan de la misma manera, pero es posible que desee utilizar un estilo de filtrado sobre otro en el código.

Filtrado mediante rangos
Puede especificar un rango para filtrar una consulta. Aquí queremos recuperar los nodos person de personas que actuaron en películas estrenadas entre 2000 y 2003:
# MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
# WHERE 2000 <= m.released <= 2003
# RETURN p.name, m.title, m.released



Filtrado por existencia de una propiedad
Recuerde que, de forma predeterminada, no es necesario que un nodo o relación tenga una propiedad determinada. Aquí hay un ejemplo de una consulta en la que solo queremos devolver los nodos Movie donde Jack Nicholson actuó en la película, y la película tiene la propiedad de eslogan.
# MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
# WHERE p.name='Jack Nicholson' AND m.tagline IS NOT NULL
# RETURN m.title, m.tagline


Filtrado por cadenas parciales
# Cypher tiene un conjunto de palabras clave relacionadas con cadenas que puede usar en las cláusulas para probar los valores de las propiedades de cadena. Puede especificar , , y .WHERESTARTS WITHENDS WITHCONTAINS

Por ejemplo, para encontrar todo los actores en el gráfico cuyo nombre de pila es Michael, escribirías:
# MATCH (p:Person)-[:ACTED_IN]->()
# WHERE p.name STARTS WITH 'Michael'  >>>>>>>>>>  STARTS WITH | ENDS WITH | CONTAINS 
# RETURN p.name


# Las pruebas de cadena distinguen entre mayúsculas y minúsculas, por lo que es posible que deba utilizar las funciones o para asegurarse de que la prueba arroje los resultados correctos. Por ejemplo:toLower()toUpper()
# MATCH (p:Person)-[:ACTED_IN]->()
# WHERE toLower(p.name) STARTS WITH 'michael'  
# RETURN p.name

Filtrado por patrones en el gráfico
# Supongamos que quisieras encontrar a todas las personas que escribieron una película pero no dirigieron esa misma película. Así es como realizaría la consulta:
# MATCH (p:Person)-[:WROTE]->(m:Movie)
# WHERE NOT exists( (p)-[:DIRECTED]->(m) )  >>>>> MUY PARECIDO A SQL CON NOT EXIST 
# RETURN p.name, m.title


Filtrado mediante listas
Si tiene un conjunto de valores con los que desea probar, puede colocarlos en una lista o puede probar con una lista existente en el gráfico. Una lista Cypher es un conjunto de valores separados por comas entre corchetes.

Puede definir la lista en la cláusula. Durante la consulta, el motor de gráficos comparará cada propiedad con los valores de la lista. Puede colocar valores numéricos o de cadena en la lista, pero normalmente, los elementos de la lista son del mismo tipo de datos. Si está probando con una propiedad de un tipo de cadena, todos los elementos de la lista serán cadenas.WHEREIN

En este ejemplo, solo queremos recuperar los nodos Person de personas nacidas en 1965, 1970 o 1975:
# MATCH (p:Person)
# WHERE p.born IN [1965, 1970, 1975]   >>>>>>>>>>>> COMO EL WHERE IN DE 
# RETURN p.name, p.born
También puede comparar un valor con una lista existente en el gráfico.

# Sabemos que la relación :ACTED_IN tiene una propiedad, roles que contiene la lista de roles que un actor tuvo en una película en particular en la que actuó. Aquí está la consulta que escribimos para devolver el nombre del actor que interpretó a Neo en la película The Matrix:

# MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
# WHERE  'Neo' IN r.roles AND m.title='The Matrix'
# RETURN p.name, r.roles


### ejemplo :  cuantos actores que nacieron luego del 1960 actuaro  en the matrix 
# MATCH (a:Person)-[:ACTED_IN]->(m:Movie) where m.title = "The Matrix" and a.born >= 1960
# RETURN count(a.name)


## ##############################################################################################

Creación de nodos
En esta lección aprenderá a escribir código Cypher para crear nodos en el gráfico.

Usando el modelo de datos De películas, creará y ejecutará código Cypher para crear actores y películas en nuestro gráfico.

# Utilizamos la palabra clave para crear un patrón en la base de datos.MERGE

# Después de la palabra clave, especificamos el patrón que queremos crear. Por lo general, esto será un solo nodo o una relación entre dos nodos.MERGE
# PODEMOS CREAR NODOS NUEVOS O RELACIONES 
Supongamos que queremos crear un nodo para representar a Michael Cain. Ejecute este código Cypher para crear el nodo.
# MERGE (p:Person {name: 'Michael Cain'})
Crea un solo nodo en el gráfico. Tenga en cuenta que cuando se utiliza para crear un nodo, debe especificar al menos una propiedad que será la clave principal única para el nodo.MERGE

# Compruebe que se ha creado el nodo.
# MATCH (p:Person {name: 'Michael Cain'})
# RETURN p
Ejecución de varias cláusulas Cypher
También podemos encadenar varias cláusulas dentro de un solo bloque de código Cypher.MERGE

# MERGE (p:Person {name: 'Katie Holmes'})
# MERGE (m:Movie {title: 'The Dark Knight'})
# RETURN p, m
Este código crea dos nodos, cada uno con una propiedad de clave principal. Debido a que hemos especificado las variables p y m, podemos usarlas en el código para devolver los nodos creados.

Usar en lugar de crear nodosCREATEMERGE
# Cypher tiene una cláusula que puede usar para crear nodos. La ventaja de usar es que no busca la clave principal antes de agregar el nodo. Puede usarlo si está seguro de que sus datos están limpios y desea una mayor velocidad durante la importación. Utilizamos en esta formación porque elimina la duplicación de nodos.CREATECREATECREATEMERGE

# CREATE ELIMINA LA DUPLICACION 


# ejercicio It’s time that we update our database.
Use the sandbox window to the right to create a new Person node for the rising star Daniel Kaluuya.
Remember that our other Person nodes contain a property called name which is considered our primary key.
# MERGE (p:Person {name:'Daniel Kaluuya'})



## ##############################################################################################
## Creación de una relación entre dos nodos
En esta lección aprenderá a escribir cláusulas Cypher para crear relaciones entre los nodos existentes en el gráfico.

Al igual que se puede utilizar para crear nodos en el gráfico, se utiliza para crear relaciones entre dos nodos. Primero debe tener referencias a los dos nodos para los que creará la relación. Al crear una relación entre dos nodos, debe tener:MERGEMERGE

# Tipo

# Dirección

# Por ejemplo, si los nodos Persona y Película ya existen, podemos encontrarlos usando una cláusula antes de crear la relación entre ellos.MATCH
# MATCH (p:Person {name: 'Michael Cain'})
# MATCH (m:Movie {title: 'The Dark Knight'})
# MERGE (p)-[:ACTED_IN]->(m) 

# Aquí encontramos los dos nodos entre los que queremos crear la relación. Luego usamos la referencia a los nodos encontrados para crear la relación ACTED_IN.

Podemos confirmar que esta relación existe de la siguiente manera:
# MATCH (p:Person {name: 'Michael Cain'})-[:ACTED_IN]-(m:Movie {title: 'The Dark Knight'})
# RETURN p, m
De forma predeterminada, en Neo4j Browser, la visualización conecta nodos que tienen relaciones entre ellos.

Observe también que no es necesario especificar la dirección en el patrón, ya que el motor de consulta buscará todos los nodos que están conectados, independientemente de la dirección de la relación.MATCH

Por ejemplo, si especificamos este patrón de relación:

# MATCH (p:Person {name: 'Michael Cain'})<-[:ACTED_IN]-(m:Movie {title: 'The Dark Knight'})
# RETURN p, m
Esta consulta no devuelve ningún nodo ya que no hay nodos con la relación ACTED_IN con los nodos Person en el gráfico.

Creación de nodos y relaciones mediante varias cláusulas
También podemos encadenar varias cláusulas dentro de un solo bloque de código Cypher.MERGE


# MERGE (p:Person {name: 'Chadwick Boseman'})
# MERGE (m:Movie {title: 'Black Panther'})
# MERGE (p)-[:ACTED_IN]-(m)
# Este código crea dos nodos y una relación entre ellos. Debido a que hemos especificado las variables p y m, podemos usarlas en el código para crear la relación entre los dos nodos.

Tenga en cuenta que en esta cláusula donde creamos las relaciones, no especificamos la dirección de la relación. De forma predeterminada, si no especifica la dirección al crear la relación, siempre se asumirá de izquierda a derecha.MERGE

Podemos confirmar que esta relación existe de la siguiente manera:

MATCH (p:Person {name: 'Chadwick Boseman'})-[:ACTED_IN]-(m:Movie {title: 'Black Panther'})
RETURN p, m
Uso para crear nodos y una relación en una sola cláusulaMERGE
Lo que sí es crear el nodo o relación si no existe en el gráfico.MERGE

Este código crea correctamente los nodos y la relación:
# MERGE (p:Person {name: 'Emily Blunt'})-[:ACTED_IN]->(m:Movie {title: 'A Quiet Place'})
# RETURN p, m
#   Puede ejecutar este código Cypher varias veces y no creará nuevos nodos o relaciones.

# ejercicio crear una relacion luego de crear 
# match (p:Person {name: "Daniel Kaluuya"}) match (m:Movie {title: "Get Out"}) merge (p)-[:ACTED_IN]->(m)

## ##############################################################################################

Actualización de propiedades
Hasta ahora, ha aprendido a crear nodos con los que se especifica la propiedad de clave principal para el nodo. Puede agregar, modificar o quitar propiedades de nodos y relaciones.MERGE

# En esta lección aprenderá a escribir código Cypher para actualizar las propiedades de los nodos y las relaciones.

# Agregar propiedades para un nodo o una relación
# Hay dos formas de establecer una propiedad para un nodo o una relación.

1. En línea como parte de la cláusulaMERGE
Ya ha visto cómo crear la propiedad de clave principal para un nodo. También puede establecer una propiedad para una relación en línea de la siguiente manera:

# MERGE (p:Person {name: 'Michael Cain'})
# MERGE (m:Movie {title: 'Batman Begins'})
# MERGE (p)-[:ACTED_IN {roles: ['Alfred Penny']}]->(m)
# RETURN p,m
En este código, el actor, Michael Cain existe, pero la película, Batman Begins no. Encontramos el nodo Persona y creamos el nodo Película. Luego, creamos la relación ACTED_IN entre el nodo Michael Cain y el nodo Batman Begins recién creado. Y establecemos la propiedad roles para esta relación en una matriz de valores, que contiene un valor, Alfred Penny.
# Observe que para la configuración de la propiedad en línea, usamos el estilo JSON de agregar los pares de clave/valor de propiedad en llaves, tal como lo hicimos cuando especificamos la propiedad para el nodo.{ .. }

2. Uso de la palabra clave para una referencia a un nodo o relaciónSET
También tenemos la opción de usar la palabra clave para establecer un valor de propiedad. En el contexto de una cláusula o particular en la que se ha definido una variable para hacer referencia al nodo o la relación, se pueden establecer valores de propiedad.SETMERGEMATCH

# MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
# WHERE p.name = 'Michael Cain' AND m.title = 'The Dark Knight'
# SET r.roles = ['Alfred Penny']
# RETURN p, r, m
Establecer varias propiedades
# Si necesita establecer varias propiedades, sepárelas con una coma (,). Por ejemplo:

# MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
# WHERE p.name = 'Michael Cain' AND m.title = 'The Dark Knight'
# SET r.roles = ['Alfred Penny'], r.year = 2008        >>>>>>>>>>>>>> es lo mismo que SQL
# RETURN p, r, m
Actualización de propiedades
Si tiene una referencia a un nodo o relación, también puede utilizarla para modificar la propiedad. Por ejemplo, si quisiéramos modificar el papel de Michael Cain para que fuera algo diferente, podríamos hacer lo siguiente:SET


# MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
# WHERE p.name = 'Michael Cain' AND m.title = 'The Dark Knight'
# SET r.roles = ['Mr. Alfred Penny']
# RETURN p, r, m
Eliminación de propiedades
# Puede quitar una propiedad de un nodo o relación mediante la palabra clave o estableciendo la propiedad en .REMOVEnull

Aquí eliminamos la propiedad roles de esta relación:

# MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
# WHERE p.name = 'Michael Cain' AND m.title = 'The Dark Knight'
# REMOVE r.roles      >>>>> ES LO MISMO QUE UN DELETE EN SQL, SOLO QUE ES REMOVE 
# RETURN p, r, m
Aquí eliminamos la propiedad nacida de un actor:

# MATCH (p:Person)
# WHERE p.name = 'Gene Hackman'
# SET p.born = null
# RETURN p
# Nunca debe quitar la propiedad que se utiliza como clave principal para un nodo.


## ##############################################################################################



Procesamiento de combinación
# Ha aprendido que puede usar para crear nodos y relaciones en el gráfico. las operaciones funcionan primero tratando de encontrar un patrón en el gráfico. Si se encuentra el patrón, los datos ya existen y no se crean. Si no se encuentra el patrón, se pueden crear los datos.MERGEMERGE

Personalización del comportamientoMERGE
También puede especificar un comportamiento en tiempo de ejecución que le permita establecer propiedades cuando se crea el nodo o cuando se encuentra el nodo. Podemos usar las condiciones o, o las palabras clave para establecer cualquier propiedad adicional.ON CREATE SETON MATCH SETSET

# En este ejemplo, si el nodo Person para McKenna Grace no existe, se crea y se establece la propiedad createdAt. Si se encuentra el nodo, se establece la propiedad updatedAt. En ambos casos, se establece la propiedad born.

// Find or create a person with this name
# MERGE (p:Person {name: 'McKenna Grace'})

// Only set the `createdAt` property if the node is created during this query
# ON CREATE SET p.createdAt = datetime()

// Only set the `updatedAt` property if the node was created previously
# ON MATCH SET p.updatedAt = datetime()

// Set the `born` property regardless
# SET p.born = 2006

RETURN p





Fusionar relaciones
Las relaciones también pueden ser complicadas.

Digamos que queremos crear un nodo Movie para representar la película, The Cider House Rules. Podríamos escribir la siguiente consulta.

Intente ejecutar este código Cypher que producirá un error:
MERGE (p:Person {name: 'Michael Cain'})-[:ACTED_IN]->(m:Movie {title: 'The Cider House Rules'})
RETURN p, m



# UNA MEJOR PRACTICA SERIA 
// Find or create a person with this name
MERGE (p:Person {name: 'Michael Cain'})

// Find or create a movie with this title
MERGE (m:Movie {title: 'The Cider House Rules'})

// Find or create a relationship between the two nodes
MERGE (p)-[:ACTED_IN]->(m)


# ejercicio  

# MERGE (m:Movie {title: 'Rocketman'})
# ON CREATE SET m.createdAt = datetime()
# ON MATCH SET m.updatedAt = datetime()
# RETURN m
## ##############################################################################################

# ELIMINACION
En una base de datos Neo4j puede eliminar:

# nodos
# relaciones
# propiedades
# etiquetas
Para eliminar cualquier dato de la base de datos, primero debe recuperarlo y luego puede eliminarlos. Ya ha aprendido a quitar o eliminar propiedades de nodos o relaciones.

## Eliminación de un nodo
Supongamos que ha creado un nodo Persona para Jane Doe.
# MATCH (p:Person)
# WHERE p.name = 'Jane Doe'
# DELETE p

# Eliminación de una relación
Supongamos que tuviéramos nuestro nodo Jane Doe de nuevo donde fue agregada como actriz en la película, The Matrix. Ejecute este código para crear el nodo y la relación.
# MATCH (p:Person {name: 'Jane Doe'})-[r:ACTED_IN]->(m:Movie {title: 'The Matrix'})
# DELETE r
# RETURN p, m

# Eliminación de un nodo y sus relaciones
Neo4j proporciona una función en la que no se puede eliminar un nodo si tiene relaciones entrantes o salientes. Esto evita que el gráfico tenga relaciones huérfanas.

MATCH (p:Person {name: 'Jane Doe'})
DETACH DELETE p
Este código elimina la relación y el nodo Persona.

También puede eliminar todos los nodos y relaciones de una base de datos con este código.


# Eliminación de etiquetas

Una práctica recomendada es tener al menos una etiqueta para un nodo, pero no más de cuatro.

A continuación, ejecute este código para agregar una nueva etiqueta a este nodo:

MATCH (p:Person {name: 'Jane Doe'})
SET p:Developer   >>>>>>>> AGREGANDO LABEL DEVELOPER
RETURN p

# MATCH (p:Person {name: 'Jane Doe'})
# REMOVE p:Developer
# RETURN p

# MATCH (p:Person {name: 'Jane Doe'})
# DETACH DELETE p


## OJO. PUEDO BORRAR UN NODO CON DELETE CUANDO NO TIENE NINUNA RELACION. PERO SI TIENE UNA RELACION, NO PUEDO DEJAR UNA RELACION COLGADA
## ENTONCES USO DETACH DELETE  QUE ME BORRAR TODAS LAS RELACIONES Y LUEGO ME BORRAR EL NODO QUE YPO QUIERO 


#  MATCH (n) DETACH DELETE n >>> BORRA TODO N

## ejercicio borrar a un actor 
MATCH (p:Person {name: 'Emil Eifrem'})
DETACH DELETE p 

## #####################################################################################################
# ¿Qué es el modelado de datos gráficos?
Si va a utilizar un gráfico Neo4j para admitir parte o la totalidad de su aplicación, debe trabajar en colaboración con sus partes interesadas para diseñar un gráfico que:

# Responda a los casos de uso clave para la aplicación.
# Proporcione el mejor rendimiento de consulta de Cypher para los casos de uso clave.


# Componentes de un gráfico Neo4j
Los componentes de Neo4j que se utilizan para definir el modelo de datos de gráficos son:

# Nodos
# Etiquetas
# Relaciones
# Propiedades

Proceso de modelado de datos
Estos son los pasos para crear un modelo de datos de gráfico:

# Comprender el dominio y definir casos de uso específicos (preguntas) para la aplicación.

# Desarrollar el modelo de datos del gráfico inicial:

# Modele los nodos (entidades).

# Modele las relaciones entre nodos.

# Pruebe los casos de uso con el modelo de datos inicial.

# Cree el gráfico (modelo de instancia) con datos de prueba mediante Cypher.

# Pruebe los casos de uso, incluido el rendimiento con respecto al gráfico.

# Refactorizar (mejorar) el modelo de datos gráficos debido a un cambio en los casos de uso clave o por razones de rendimiento.

# Implemente la refactorización en el gráfico y vuelva a probar usando Cypher.

El modelado de datos de gráficos es un proceso iterativo. El modelo de datos de gráfico inicial es un punto de partida, pero a medida que aprenda más sobre los casos de uso o si los casos de uso cambian, el modelo de datos de gráfico inicial deberá cambiar. Además, puede encontrar que, especialmente cuando el gráfico escala, deberá modificar el gráfico (refactorizar) para lograr el mejor rendimiento para sus casos de uso clave.

La refactorización es muy común en el proceso de desarrollo. Un gráfico Neo4j tiene un esquema opcional que es bastante flexible, a diferencia del esquema en un RDBMS. Un desarrollador de Cypher puede modificar fácilmente el gráfico para representar un modelo de datos mejorado.

## #####################################################################################################

Descripción del dominio de la aplicación
Antes de comenzar el proceso de modelado de datos, debe:

# Identificar a las partes interesadas y desarrolladores de la aplicación.

# Con las partes interesadas y los desarrolladores:

# Describa la aplicación en detalle.

# Identificar a los usuarios de la aplicación (personas, sistemas).

# Acordar los casos de uso de la aplicación.

# Clasificar la importancia de los casos de uso.


# Dominio de la película
En el curso, Neo4j Fundamentals, se le presentó un gráfico de película "inicial".

El dominio incluye películas, personas que actuaron o dirigieron películas y usuarios que calificaron películas. Lo que hace que este dominio sea interesante son las conexiones o relaciones entre nodos en el gráfico.

# Casos de uso
La mayoría de los casos de uso de una aplicación se pueden enumerar mediante una lista completa de preguntas. Los casos de uso ayudan a definir cómo se comportará la aplicación en tiempo de ejecución.

Estos son los casos de uso con los que trabajará para desarrollar el modelo de datos de gráfico inicial:

¿Qué personas actuaron en una película?

¿Qué persona dirigió una película?

¿En qué películas actuó una persona?

¿Cuántos usuarios calificaron una película?

¿Quién fue la persona más joven en actuar en una película?

¿Qué papel jugó una persona en una película?

¿Cuál es la película mejor calificada en un año en particular según imDB?

¿En qué películas dramáticas actuó un actor?

¿Qué usuarios le dieron a una película una calificación de 5?


## #####################################################################################################
### MUY IMPORTANTE ###

Tipos de modelos
Al realizar el proceso de modelado de datos de gráficos para una aplicación, necesitará al menos dos tipos de modelos:

# Modelo de datos
# Modelo de instancia

# >>> Modelo de datos
El modelo de datos describe las etiquetas, las relaciones y las propiedades del gráfico. No tiene datos específicos que se crearán en el gráfico.

Aquí hay un ejemplo de un modelo de datos:

Modelo de datos
No hay nada que identifique de forma única un nodo con una etiqueta determinada. Sin embargo, un modelo de datos de gráfico es importante porque define los nombres que se usarán para las etiquetas, los tipos de relación y las propiedades cuando la aplicación cree y use el gráfico


# Directrices de estilo para el modelado
Al comenzar el proceso de modelado de datos de gráficos, es importante que acepte cómo se nombran las etiquetas, los tipos de relación y las claves de propiedad. Las etiquetas, los tipos de relación y las claves de propiedad distinguen entre mayúsculas y minúsculas, a diferencia de las palabras clave Cypher que no distinguen entre mayúsculas y minúsculas.

Una práctica recomendada de Neo4j es usar lo siguiente cuando nombra los elementos del gráfico, pero puede usar cualquier convención para su aplicación.

# Una etiqueta es un identificador único que comienza con una letra mayúscula y puede ser CamelCase.

# Ejemplos: Persona, Empresa, GitHubRepo

# Un tipo de relación es un identificador único que está en mayúsculas con el carácter de subrayado.

# Ejemplos: SIGUE, MARRIED_TO

# Una clave de propiedad para un nodo o una relación es un identificador único que comienza con una letra minúscula y puede ser camelCase.

# Ejemplos: deptId, firstName

# Nota: Los nombres de clave de propiedad no tienen por qué ser únicos. Por ejemplo, un nodo Persona y un nodo Película, cada uno puede tener la clave de propiedad de tmdbId.

# Modelo de instancia
Una parte importante del proceso de modelado de datos de gráficos es probar el modelo contra los casos de uso. Para hacer esto, debe tener un conjunto de datos de muestra que pueda usar para ver si los casos de uso se pueden responder con el modelo.

A continuación se muestra un ejemplo de un modelo de instancia:

Modelo de instancia
En este modelo de instancia, hemos creado algunas instancias de los nodos Persona y Película, así como sus relaciones. Tener este tipo de modelo de instancia ayudará a probar nuestros casos de uso.



## #####################################################################################################

## Definición de etiquetas
Las entidades son los sustantivos dominantes en los casos de uso de la aplicación

En el dominio Película, usamos los sustantivos en nuestros casos de uso para definir las etiquetas, por ejemplo:

¿Qué personas actuaron en una película?

¿Qué persona dirigió una película? # >>>> los verbos son las relaciones

¿En qué películas actuó una persona?

--------------------------------------------

# Propiedades del nodo
Las propiedades de nodo se utilizan para:
# Identifique de forma única un nodo.
# Responda detalles específicos de los casos de uso de la aplicación.
# Datos de devolución.

Anclaje (dónde comenzar la consulta).

MATCH (p:Person {name: 'Tom Hanks'})-[:ACTED_IN]-(m:Movie) RETURN m

Recorre el gráfico (navegación).

MATCH (p:Person)-[:ACTED_IN]-(m:Movie {title: 'Apollo 13'})-[:RATED]-(u:User) RETURN p,u

Devolver datos de la consulta.

MATCH (p:Person {name: 'Tom Hanks'})-[:ACTED_IN]-(m:Movie) RETURN m.title, m.released

# Identificadores únicos en el gráfico De película
En el gráfico Película, utilizamos las siguientes propiedades para identificar de forma única nuestros nodos:

Person.tmdbId

Movie.tmdbId

Propiedades de los nodos
Además del tmdbId que se utiliza para identificar de forma única un nodo, debemos revisar los casos de uso para determinar los tipos de datos que debe contener un nodo.

Aquí hay una lista de nuestros casos de uso específicos para los nodos Persona y Película en los que nos centraremos. Estos casos de uso nos informan sobre los datos que necesitamos en los nodos Película y Persona.

## ejercicio crear nuevos nodos 
# MERGE (:Movie {title: 'Apollo 13', tmdbId: 568, released: '1995-06-30', imdbRating: 7.6, genres: ['Drama', 'Adventure', 'IMAX']})
# MERGE (:Person {name: 'Tom Hanks', tmdbId: 31, born: '1956-07-09'})
# MERGE (:Person {name: 'Meg Ryan', tmdbId: 5344, born: '1961-11-19'})
# MERGE (:Person {name: 'Danny DeVito', tmdbId: 518, born: '1944-11-17'})
# MERGE (:Person {name: 'Jack Nicholson', tmdbId: 514, born: '1937-04-22'})
# MERGE (:Movie {title: 'Sleepless in Seattle', tmdbId: 858, released: '1993-06-25', imdbRating: 6.8, genres: ['Comedy', 'Drama', 'Romance']})
# MERGE (:Movie {title: 'Hoffa', tmdbId: 10410, released: '1992-12-25', imdbRating: 6.6, genres: ['Crime', 'Drama']})


## ejercicio crear dos nodos con atributos name y id 
# MERGE (:User {userId: 534, name : 'Sandy Jones'}) 
# MERGE (:User {userId: 105, name: 'Clinton Spencer'})



## #####################################################################################################


## Las relaciones son conexiones entre entidades

Elegir buenos nombres (tipos) para las relaciones en el gráfico es importante. Los tipos de relación deben ser algo que sea intuitivo tanto para las partes interesadas como para los desarrolladores. Los tipos de relación no se pueden confundir con un nombre de entidad.

Entonces, en nuestros casos de uso de ejemplo, podríamos definir estos tipos de relación:

USOS

CASADO

# Al crear una relación en Neo4j, una dirección debe especificarse explícitamente o inferirse por la dirección de izquierda a derecha en el patrón especificado. En tiempo de ejecución, durante una consulta, normalmente no se requiere dirección.

# La relación MARRIED podría crearse para comenzar en cualquiera de los nodos, ya que este tipo de relación es simétrica.
# Una relación es típicamente entre 2 nodos diferentes, pero también puede ser al mismo nodo.

# El principal riesgo del fanout es que puede conducir a nodos muy densos o supernodos. Estos son nodos que tienen cientos de miles de relaciones entrantes o salientes Los Supernodos deben manejarse con cuidado.

Propiedades para las relaciones
Las propiedades de una relación se utilizan para enriquecer la forma en que se relacionan dos nodos. Cuando se define una propiedad para una relación, se debe a que los casos de uso hacen una pregunta específica sobre cómo se relacionan dos nodos, no solo porque están relacionados.

Por ejemplo, vimos en el curso Fundamentos de Neo4j que se pueden agregar propiedades a una relación para describirla más a fondo.

Propiedades de relación en el gráfico de película
Al igual que se analizan los casos de uso para nombrar etiquetas, tipos de relaciones y propiedades de nodo, se utilizan los casos de uso para crear propiedades para las relaciones.

Aquí hay un caso de uso:

¿Qué papel jugó una persona en una película?

Las operaciones en tiempo de ejecución para este caso de uso son:

Recuperar el nombre de la persona.

Sigue las relaciones ACTED_IN a las películas.

Filtra la película por su título.

Devuelva el rol de la relación ACTED_IN entre los dos nodos.

Sabemos que el papel de una relación ACTED_IN en particular será necesario para este caso de uso. Por lo tanto, agregamos la propiedad de rol a esta relación. Aquí está el modelo de datos:


### ehercitacion 
# MATCH (apollo:Movie {title: 'Apollo 13'})
# MATCH (tom:Person {name: 'Tom Hanks'})
# MATCH (meg:Person {name: 'Meg Ryan'})
# MATCH (danny:Person {name: 'Danny DeVito'})
# MATCH (sleep:Movie {title: 'Sleepless in Seattle'})
# MATCH (hoffa:Movie {title: 'Hoffa'})
# MATCH (jack:Person {name: 'Jack Nicholson'})

// create the relationships between nodes
# MERGE (tom)-[:ACTED_IN {role: 'Jim Lovell'}]->(apollo)
# MERGE (tom)-[:ACTED_IN {role: 'Sam Baldwin'}]->(sleep)
# MERGE (meg)-[:ACTED_IN {role: 'Annie Reed'}]->(sleep)
# MERGE (danny)-[:ACTED_IN {role: 'Bobby Ciaro'}]->(hoffa)
# MERGE (danny)-[:DIRECTED]->(hoffa)
# MERGE (jack)-[:ACTED_IN {role: 'Jimmy Hoffa'}]->(hoffa)



## otra ejercitacion, crear relaciones con atributos 
MATCH (sandy:User {name: 'Sandy Jones'})
MATCH (clinton:User {name: 'Clinton Spencer'})
MATCH (apollo:Movie {title: 'Apollo 13'})
MATCH (sleep:Movie {title: 'Sleepless in Seattle'})
MATCH (hoffa:Movie {title: 'Hoffa'})
MERGE (sandy)-[:RATED {rating:4}]->(sleep) 
MERGE (sandy)-[:RATED {rating:5}]->(apollo) 
MERGE (clinton)-[:RATED {rating:3}]->(apollo)
MERGE (clinton)-[:RATED {rating:3}]->(sleep)  
MERGE (clinton)-[:RATED {rating:3}]->(hoffa)  


## #####################################################################################################


En el siguiente desafío, probará cada caso de uso contra el gráfico ejecutando consultas cypher.

Su prueba consistirá en ejecutar código Cypher en el modelo de instancia para verificar que el gráfico y la consulta admitan el caso de uso.

Por ejemplo, con nuestro primer caso de uso:

Caso de uso #1: ¿Qué personas actuaron en una película?

Ejecutará esta consulta donde especifique el título de la película:

¿Más pruebas?
A medida que revisa los casos de uso, puede pensar en más datos que desea agregar al gráfico para completar las pruebas.

El código Cypher utilizado para probar los casos de uso debe revisarse cuidadosamente para verificar su corrección. Además, debe comprender que si y cuando se refactoriza el gráfico (siguiente módulo), es posible que sea necesario modificar el código Cypher para estos casos de uso para mejorar el rendimiento.

Las pruebas básicas para garantizar que los casos de uso puedan ser respondidos por el modelo de datos es el primer paso de las pruebas.

Un factor realmente importante al probar el gráfico es la escalabilidad. ¿Cómo funcionarán estas consultas si el gráfico tiene millones de nodos o relaciones? Aquí es donde debe trabajar con los desarrolladores de Cypher para probar el rendimiento de las consultas cuando el gráfico crece.

## ejercitacion 
# 1: What people acted in a movie?
MATCH (p:Person)-[:ACTED_IN]-(m:Movie)
WHERE m.title = 'Sleepless in Seattle'
RETURN p.name AS Actor

# 2: What person directed a movie?
MATCH (p:Person)-[:DIRECTED]-(m:Movie)
WHERE m.title = 'Hoffa'
RETURN  p.name AS Director

# 3: What movies did a person act in?
MATCH (p:Person)-[:ACTED_IN]-(m:Movie)
WHERE p.name = 'Tom Hanks'
RETURN m.title AS Movie

# 4: How many users rated a movie?  
MATCH (u:User)-[:RATED]-(m:Movie)
WHERE m.title = 'Apollo 13'
RETURN count(*) AS `Number of reviewers`

# 5: Who was the youngest person to act in a movie?   
MATCH (p:Person)-[:ACTED_IN]-(m:Movie)
WHERE m.title = 'Hoffa'
# RETURN  p.name AS Actor, p.born as `Year Born` ORDER BY p.born DESC LIMIT 1    ### IGUAL A SQL| AS| ORDER BY | LIMIT ####



# 8: What drama movies did an actor act in?
MATCH (p:Person)-[:ACTED_IN]-(m:Movie)
WHERE p.name = 'Tom Hanks' AND
'Drama' IN m.genres
RETURN m.title AS Movie



## #####################################################################################################



¿Por qué refactorizar?
La refactorización es el proceso de cambiar el modelo de datos y el gráfico.

Hay tres razones por las que refactorizaría:
# El gráfico tal como está modelado no responde a todos los casos de uso.
# Ha surgido un nuevo caso de uso que debe tener en cuenta en su modelo de datos.
# El Cypher para los casos de uso no funciona de manera óptima, especialmente cuando el gráfico escala

Pasos para la refactorización
# Diseñar el nuevo modelo de datos.
# Escriba código Cypher para transformar el gráfico existente e implementar el nuevo modelo de datos.
# Vuelva a probar todos los casos de uso, posiblemente con el código Cypher actualizado.



## #####################################################################################################


Etiquetas en tiempo de ejecución
# MATCH (n) RETURN n devuelve todos los nodos del gráfico.
# MATCH (n:Person) RETURN n devuelve todos los nodos Persona del gráfico.

Si los nodos de persona también tuvieran una etiqueta que es el país del que proviene una persona, entonces podría usar este código Cypher para recuperar a todas las personas de los EE. UU.:
# MATCH (n:Person) WHERE n.country = 'US' RETURN n


No abusar de las etiquetas
Debe usar las etiquetas sabiamente en su modelo de datos. Deben usarse si ayudará con la mayoría de sus casos de uso. Una práctica recomendada es limitar el número de etiquetas de un nodo a 4.

Aquí hay un ejemplo de uso excesivo de etiquetas en el modelo de datos:

Aquí vemos nodos de persona que tienen una etiqueta que representa el país del que proviene una persona como describimos anteriormente.

Además, vemos varias etiquetas para los nodos De película. La etiqueta representa los idiomas disponibles para una película.



# Refactorizar el gráfico
Con Cypher, puede transformar fácilmente el gráfico. Con este código, que ejecutarás en el próximo Reto, encontramos todos los nodos Persona que tienen una relación ACTED_IN. A continuación, establecemos una etiqueta para el nodo.
# MATCH (p:Person)
# WHERE exists ((p)-[:ACTED_IN]-())
# SET p:Actor





## conclusion ## 
Un nodo puede tener mas de un label, 
no se pueden parametrizar un laber. es decir no puedo usar un label en where, me da error 
un ejemplo de dos laberl seria Person, Actor 
# PROFILE MATCH  ---> ME DA EL PLAN DE EJECUCION



## #####################################################################################################

## no usar labels asi
 ## NO PONER JERARQUIAS
 ## SEMANTICAMENTE ORTOGONALES



#############################
#############################
## ########################################################## ############################################ ####################################
VISUAL DE NEO 4J

# 1) MENU DE PROJECTOS 
Un proyecto en el escritorio es una representación de una carpeta de desarrollo en el disco. Puede crear sistemas de administración de bases de datos locales (DBMS), conectarse a DBMS remotos y agregar archivos dentro de su proyecto. Neo4j Desktop le permite administrar múltiples proyectos y es fácil mover tanto DBMS como archivos entre diferentes proyectos arrastrando y soltando. Sin embargo, solo puede tener un DBMS activo o una conexión remota a la vez.

Cada DBMS de un proyecto contiene una lista de sus bases de datos, que se expande cuando se selecciona un DBMS. Si se detiene el DBMS, la lista de bases de datos se almacena en caché. A continuación, la lista se actualiza de nuevo al iniciar el DBMS. Sin embargo, para los dbMS nuevos, la lista de bases de datos no está disponible hasta que el DBMS se haya iniciado correctamente por primera vez.

# 2) DBMS
Un DBMS, sistema de gestión de bases de datos, es una instancia de servidor Neo4j que contiene un mínimo de la base de datos y una base de datos predeterminada. Tras la creación de un DBMS, se llama a la base de datos predeterminada , pero puede cambiarle el nombre o crear una nueva base de datos como predeterminada. También se puede acceder a los DBMS existentes a través del menú DBMS.systemneo4j

Un DBMS, sistema de gestión de bases de datos, es una instancia de servidor Neo4j que contiene un mínimo de la base de datos y una base de datos predeterminada. Tras la creación de un DBMS, se llama a la base de datos predeterminada , pero puede cambiarle el nombre o crear una nueva base de datos como predeterminada. También se puede acceder a los DBMS existentes a través del menú DBMS.systemneo4j

Del mismo modo, los archivos de registro; , , y también se puede ver directamente desde el escritorio, desde el menú Más opciones. Esto abre una ventana separada que muestra el archivo de registro seleccionado. También puede acceder a los registros desde → .debug.logneo4j.logquery.logsecurity.logLogsOpen folderLogs

# 3) Conexión remota
Además de administrar DBMS locales, Neo4j Desktop también le permite conectarse a una instancia remota. Esta puede ser una instancia que se ejecuta en GCE, Aura o alojada en una red local, por ejemplo. La conexión remota utiliza el protocolo.bolt

Se puede acceder a las conexiones remotas para cada proyecto, en el menú desplegable -. Consulte Conectarse a un DBMS remoto para obtener más información sobre cómo conectarse a una instancia remota.Add


# 4) Aplicaciones gráficas
Hay varias formas de interactuar con el gráfico. Una forma es usar una aplicación Graph y Desktop viene incluido con dos de estas aplicaciones, Neo4j Browser y Bloom. Por favor, vea el Documentación del navegador y el Documentación de Bloom para más información. Neo4j Browser y Bloom se utilizan para visualizar y consultar el gráfico, pero otras aplicaciones ofrecen herramientas de importación para bases de datos relacionales, herramientas de monitoreo y analizadores de registros de consultas, por ejemplo. Puede seleccionarlos e instalarlos desde una lista seleccionada en la Galería de aplicaciones graph en el escritorio.



# 5. Archivos
# Además de agregar DBMS, Desktop también le permite agregar archivos y carpetas a su proyecto. 
# Estos pueden ser archivos Cypher y guías del navegador Neo4j que se abrirán en el navegador Neo4j cuando haga clic en ellos. 
Además, también puede agregar archivos de volcado de base de datos a esta sección. Los archivos de volcado se pueden utilizar para restaurar un DBMS y, por lo tanto, agregarlo a su proyecto.

# Para agregar archivos, puede usar el menú desplegable en su proyecto o puede arrastrar y soltar los archivos en la sección. Si coloca archivos en la carpeta Proyecto, por ejemplo, con su administrador de archivos o desde la línea de comandos, Desktop los recogerá y los mostrará en esta sección. El menú desplegable le permite filtrar los archivos y carpetas agregados por nombre, tamaño, fecha de creación, fecha de la última modificación o fecha en que se abrió por última vez.AddFile

archivos
Puede mover sus archivos fácilmente entre proyectos arrastrando un archivo de esta sección y soltándolo en un proyecto diferente en el menú Proyecto de la barra latera

# -##########################################################################################################################

### Crear y administrar un nuevo DBMS localmente ### 
Cuando abre Neo4j Desktop por primera vez con el objetivo de crear un nuevo DBMS, necesita tener un proyecto para su DBMS. En el menú de la barra lateral, seleccione un proyecto existente o cree uno nuevo. Una vez que tenga un proyecto abierto, puede agregarle un nuevo DBMS desde el menú desplegable de su proyecto.ProjectsAdd

# CREO UN PROYECTO PREFERIBLEMENTE DESDE EL DIRECTORIO
# VOY A ADD (ARRIBA A LA DERECHA ) >>>N ELIJO DE DONDE SACO LA DBMS

Desktop requiere que cree una contraseña para su nuevo DBMS y seleccione una versión de Neo4j. Tenga en cuenta que si selecciona cualquier versión que no sea la predeterminada, Desktop necesita descargar recursos y, por lo tanto, debe estar conectado a Internet.

# creo la base de datos BASE-PROYECTO1 para el proyecto 1 y ya esta 


## tener en cuent aque tambien nbos podemos conectar de forma remota 


# -##########################################################################################################################
# -##########################################################################################################################
# -##########################################################################################################################

# ELIMINANDO DATOS DUPLICADOS 

This query finds all movies in Italian:

MATCH (m:Movie)
WHERE 'Italian' IN m.languages
RETURN m.title


# Tenemos un nodo pelicula con atributo idioma y eso lo queremos refactorizar y pasarlo a  un nuevo novo 

# usamos la clausula UNWIND 
Este código itera a través de todos los nodos De película 
y crea un nodo de lenguaje para cada idioma que encuentra y, a continuación, crea la relación entre el nodo De película y el nodo De idioma mediante la relación de IN_LANGUAGE. Utiliza la cláusula Cypher para separar cada elemento de la lista de propiedades languages en un valor de fila independiente que se procesa más adelante en la consulta.UNWIND

# MATCH (m:Movie)
# UNWIND m.languages AS language
# WITH  language, collect(m) AS movies
# MERGE (l:Language {name:language})
# WITH l, movies
# UNWIND movies AS m
# WITH l,m
# MERGE (m)-[:IN_LANGUAGE]->(l);
# MATCH (m:Movie)
# SET m.languages = null

## ejerccio lo mismo pero con las peliculas 
MATCH (m:Movie)
UNWIND m.genres AS genres
WITH genres, collect(m) AS movies
MERGE (g:Genres {name:genres})
WITH g, movies
UNWIND movies AS m
WITH g,m
MERGE (m)-[:IN_LANGUAGE]->(g)



# -##########################################################################################################################
# eliminando datos complejos 
por ejemplo si quiero refactorizar ACTENIN anadiendo el anio,n hago lo siguiente :

# MATCH (n:Actor)-[r:ACTED_IN]->(m:Movie)
# CALL apoc.merge.relationship(n,
#                               'ACTED_IN_' + left(m.released,4),
#                               {},
#                               m ) YIELD rel
# RETURN COUNT(*) AS `Number of relationships merged`


# ES BASICAMENTE UN PROCEDURE



Tiene un procedimiento que le permite crear dinámicamente relaciones en el gráfico. Utiliza los 4 caracteres más a la izquierda de la propiedad liberada para un nodo Movie para crear el nombre de la relación.apoc.merge.relationship


MATCH (p:Actor)-[:ACTED_IN_1995]-(m:Movie)
WHERE p.name = 'Tom Hanks'
RETURN m.title AS Movi

# EJERCITACION Execute the following code to create a new set of relationships based on the year of the released property for each Node.

For example, Apollo 13 was released in 1995, so an additional ACTED_IN_1995 will be created between Apollo 13 and any actor that acted in the movie.


MATCH (n:Actor)-[:ACTED_IN]->(m:Movie)
CALL apoc.merge.relationship(n,
  'ACTED_IN_' + left(m.released,4),
  {},
  {},
  m ,
  {}
) YIELD rel
RETURN count(*) AS `Number of relationships merged`;


# -##########################################################################################################################

# ANADIENDO NODOS INTERMEDIOS 
Puede crear nodos intermedios cuando necesite:

# Conecte más de dos nodos en un solo contexto.
# Hiperbordes (relaciones n-arias)
# Relaciona algo con una relación.
# Compartir datos en el gráfico entre entidades.


En Neo4j, no hay forma de crear una relación que conecte una relación con un tercer nodo. Las relaciones Neo4j solo pueden conectar dos nodos.


# ejercicio
Find an actor that acted in a Movie (MATCH (a:Actor)-[r:ACTED_IN]→(m:Movie))

Create (using MERGE) a Role node setting it’s name to the role in the ACTED_IN relationship.

Create (using MERGE) the PLAYED relationship between the Actor and the Role nodes.

Create (using MERGE) the IN_MOVIE relationship between the Role and the Movie nodes.

# -##########################################################################################################################
# cargar csv --> LOAD CSV

Los tipos de datos que puede almacenar como propiedades en Neo4j incluyen:

Cuerda

Largo (valores enteros)
Doble (valores decimales)
Booleano
Fecha/Fecha y hora
Punto (espacil)
StringArray (lista de cadenas separadas por comas)
LongArray (lista de valores enteros separados por comas)
DoubleArray (lista de valores decimales separados por comas)


# requisitos para importar datos CSV
Debe tener uno o más archivos CSV que representen los nodos y las relaciones que se crearán en el gráfico. También debe tener un DBMS Neo4j existente que se haya iniciado. Por lo general, comienza con un gráfico que no tiene nada en él.

En este curso, no creará los archivos de datos de origen para la importación, pero utilizará archivos que ya se han creado para usted.

# FIELDTERMINATOR   ---> el delimitador 


IDs must be unique
When you load data from CSV files, you rely heavily upon the IDs specified in the file. A Neo4j best practice is to use an ID as a unique property value for each node.

# LOAD CSV WITH HEADERS
# FROM 'https://data.neo4j.com/importing/ratings.csv'
# AS row
# RETURN count(row)


# https://www.youtube.com/watch?v=J8vmqJrqd6w

# What is a multi-value property?
A multi-value property is a property that can hold one or more values. This type of data in Neo4j is represented as a list. All values in a list must have the same type. For example:

["USA", "Germany", "France"]

[100, 55, 4]

Transforming list properties
Transforming multi-value fields as lists can be done as follows where we use two Cypher built-in functions to help us:

Cypher
MATCH (m:Movie)
SET m.countries = split(coalesce(m.countries,""), "|"),
m.languages = split(coalesce(m.languages,""), "|"),
m.genres = split(coalesce(m.genres,""), "|")
coalesce() returns an empty string if the entry in m.countries is null. split() identifies each element in the multi-value field where the "|" character is the separator and create a list of each elemen


## anadir nuevar etiquetas

Adición de las etiquetas
Aquí está el código que podemos usar para agregar la etiqueta Actor a todos los nodos que tienen la relación ACTED_IN:

# MATCH (p:Person)-[:ACTED_IN]->()
# WITH DISTINCT p
# SET p:Actor   >>> NPTAR QUE SON DOS PUNTOS Y EMPIEZA CON MAYUSCULA ES UN LABEL


##constrains
Adding a uniqueness constraint for Genre nodes
When you used the Data Importer, it automatically created the uniqueness constraints in the graph for the unique IDs you specified when you imported the data.

You can view the constraints defined in the graph with the 
# SHOW CONSTRAINTS command in Neo4j Browser:

# CREATE CONSTRAINT Genre_name ON (g:Genre) ASSERT g.name IS UNIQUE

# Creating the Genre nodes from the genres property of Movie nodes

# The UNWIND clause expands the elements in genres list for the node as rows. With this data, it creates the Genre node using MERGE. With MERGE, it only creates the node if it does not already exist. Then it creates the relationship between the Movie node and the Genre node.

MATCH (m:Movie)
UNWIND m.genres AS genre
WITH m, genre
MERGE (g:Genre {name:genre})
MERGE (m)-[:IN_GENRE]->(g)
# Removing the genres property
MATCH (m:Movie)
SET m.genres = null




