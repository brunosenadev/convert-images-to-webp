
# Conversor de Imagens para WebP

Este projeto foi criado a partir da necessidade de converter diversas imagens para o formato WebP com o objetivo de otimizar o desempenho de uma landing page. Durante o desenvolvimento dessa página, percebi que o uso de imagens em alta qualidade estava impactando o tempo de carregamento e a performance da página. O WebP, por ser um formato com uma boa relação entre qualidade e compressão, se mostrou uma excelente alternativa para resolver esse problema.

## Objetivo

Automatizar a conversão de imagens em formatos como PNG, JPG e JPEG para o formato WebP. Esse processo foi essencial para melhorar o tempo de carregamento e a performance da landing page, garantindo uma experiência mais ágil e eficiente para os usuários.
## Tecnologias Utilizadas

- **Python**: A linguagem escolhida para automatizar o processo de conversão.
- **Pillow**: Biblioteca Python para manipulação e conversão de imagens.
- **WebP**: Formato de imagem com alta compressão e qualidade, ideal para o uso na web.


## Como Funciona
O script percorre os diretórios de imagens e converte automaticamente os arquivos para o formato WebP. Ele cria as pastas de destino se necessário e organiza as imagens convertidas de forma a manter a estrutura original.

### Passos do Processo:
 **1.** O script verifica se o diretório de destino para as imagens WebP existe, se não, ele cria o diretório.

**2.** Para cada subpasta encontrada no diretório de origem, o script cria uma subpasta correspondente no diretório de destino.

**3.** O script percorre as imagens e as converte para WebP, utilizando a biblioteca Pillow.

**4.** As imagens convertidas são nomeadas de forma sequencial para garantir organização.
## Requisitos
- Python 3.x
- Biblioteca Pillow (PIL)

    Para instalar a biblioteca Pillow, execute:
    ```
        pip install pillow
    ```
## Como Usar
**1.** Coloque as imagens a serem convertidas em pastas dentro de um diretório de origem.

**2.** Defina o caminho do diretório de origem e do diretório de destino dentro do código, nas variáveis directory e directory_webp, respectivamente.

**3.** Execute o script para realizar a conversão.

```
    python convert_images.py
```
## Exemplo de Estrutura de Diretórios
```
diretorio/
  ├── empresa_a/
  │   ├── imagem1.png
  │   ├── imagem2.jpg
  │   └── imagem3.jpeg
  ├── empresa_b/
  │   ├── imagem1.png
  │   └── imagem2.jpg
  └── empresa_c/
      ├── imagem1.png
      └── imagem2.jpg
```
Após a execução do script:
```
diretorio_de_destino/
  ├── empresa_a/
  │   ├── empresa_a-1.webp
  │   ├── empresa_a-2.webp
  │   └── empresa_a-3.webp
  ├── empresa_b/
  │   ├── empresa_b-1.webp
  │   └── empresa_b-2.webp
  └── empresa_c/
      ├── empresa_c-1.webp
      └── empresa_c-2.webp
```