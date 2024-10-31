# <center>Visão Computacional</center>
![Imagem](https://community.revelo.com.br/content/images/size/w2000/2022/03/-15--COVER---Reconhecimento-de-padro-es-em-visa-o-computacional-via-Template-Matching.png)
Projeto de pesquisa [04/2024/PROPPG](https://proppg.ifpa.edu.br/documentos-e-formularios/pesquisa/editais-2024/edital-n-04-2024-proppg/2592-edital-n-04-2024-campus-itaituba-assinado/file) | Visão Computacional | Matemática | Interativa e Adaptativa

###  No momento estou usando [pdm](https://pdm-project.org/latest/) como gerenciador de dependências e a biblioteca base de desenvolvimento do projeto é a [mediapipe](https://chuoling.github.io/mediapipe/).

### O [requirements.txt](requirements.txt) está disponível.

### Como usar:
### Cada dedo tem um código numérico que inicia-se do 0 ate o 4, começando do polegar até o dedo mínimo respectivamente.

![Imagem](https://www.educlub.com.br/rails/active_storage/representations/redirect/BAh7BkkiC19yYWlscwY6BkVUewdJIglkYXRhBjsAVGkCigdJIghwdXIGOwBUSSIMYmxvYl9pZAY7AEY=--df8b41624182bf6b09831943487862635a780632/BAh7BkkiC19yYWlscwY6BkVUewdJIglkYXRhBjsAVHsHOgtmb3JtYXQ6CHBuZzoUcmVzaXplX3RvX2xpbWl0WwdpAhACaQIQAkkiCHB1cgY7AFRJIg52YXJpYXRpb24GOwBG--b70087bc94213e0515c5430ed18c83dce2987676/Nome%20dos%20dedos%20das%20m%C3%A3os.webp)

### Apenas o dedo(s) indicado(s) elevado(s).

#### 1 = indicador;
#### 2 = indicador e dedo médio;
#### 3 = indicador, dedo médio e anelar;
#### 4 = indicador, dedo médio, anelar e dedo mínimo;
#### 5 = indicador, dedo médio, anelar, dedo mínimo e polegar;
#### 6 = polegar;
#### 7 = polegar e indicador;
#### 8 = polegar, indicador e dedo médio;
#### 9 = polegar, indicador, dedo médio e anelar;
#### 0 = polegar e dedo médio;
#### + (soma) = anelar;
#### - (Subtração) =  anelar e dedo médio;
#### * (Multiplicação) = polegar, indicador e dedo minímo;
#### / (Divisão) = indicador e dedo minímo;
#### = (igualdade) = dedo médio, anelar e dedo mínimo.

## OBS: Caso queira inserir dezena e centema... basta manter o(s) dedo(s) elevados.