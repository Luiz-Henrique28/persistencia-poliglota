Abordagem Recomendada: Duas Seções na Interface
Você pode dividir a sua interface do Streamlit em duas seções principais: uma para cadastro e outra para consulta e geo-processamento. Isso mantém a lógica clara e o usuário não se confunde.

1. Seção de Cadastro
Esta seção é para inserir novos dados. Ela terá dois formulários, um para cada banco de dados.


Cadastro no SQLite: Um formulário para o usuário adicionar novas cidades e estados.


Cadastro no MongoDB: Um formulário separado para adicionar novos locais de interesse, onde o usuário vai inserir o nome, a descrição, as coordenadas (latitude e longitude) e selecionar a cidade e o estado a partir de uma lista pré-existente (populada pelo SQLite).

Essa separação é prática porque o projeto pede para cadastrar dados em ambos os bancos.

2. Seção de Consulta e Geo-processamento
Esta seção será o "motor" do seu projeto, onde a magia acontece.


Seleção de Cidade: O usuário escolherá uma cidade que está no seu banco de dados SQLite.


Visualização de Locais: Com base na cidade selecionada, o sistema vai buscar no MongoDB os locais de interesse associados a ela e mostrá-los em um mapa.


Cálculo de Proximidade: Você terá um formulário onde o usuário poderá informar uma coordenada e um raio de distância (por exemplo, 10 km). A aplicação então listará todos os locais do MongoDB que estão dentro daquele raio