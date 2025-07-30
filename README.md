# Projeto de Álgebra Linear Aplicada à Engenharia de Computação:
## Filtros de Imagem Digitais com Convolução Matricial

Este repositório contém um projeto desenvolvido para a disciplina de Álgebra Linear no curso de Engenharia de Computação. O objetivo principal é demonstrar a aplicação prática de conceitos de Álgebra Linear, em particular **matrizes** e a operação de **convolução**, na implementação de filtros de imagem digitais.

---

## 🚀 Motivação

Filtros de imagem são amplamente utilizados em diversas aplicações computacionais, desde redes sociais (Instagram, TikTok) e edição de fotos até sistemas de visão computacional em robótica e medicina. Este projeto explora a base matemática por trás desses filtros, revelando como operações matriciais simples podem transformar significativamente a aparência de uma imagem.

---

## ✨ Conceitos de Álgebra Linear Aplicados

O coração deste projeto reside na utilização dos seguintes conceitos:

* **Representação de Imagens como Matrizes:** Imagens digitais são fundamentalmente matrizes de pixels, onde cada elemento numérico representa a intensidade de cor. Para imagens coloridas (RGB), podemos visualizar isso como múltiplas matrizes (uma para cada canal de cor).
* **Kernels (Máscaras de Filtro):** São pequenas matrizes que definem a operação de um filtro específico.
* **Convolução:** É a operação matricial chave. Um kernel "desliza" sobre a imagem, realizando multiplicações elemento a elemento e somas ponderadas em cada "janela" de pixels. O resultado dessa soma substitui o pixel central da janela na imagem de saída.

---

## 🛠️ Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina.

### Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.x recomendada). As seguintes bibliotecas Python são necessárias:

* `numpy`
* `Pillow` (PIL Fork)

Você pode instalá-las usando `pip`:

```bash
pip install numpy Pillow
````

### Instalação

1.  Clone este repositório para o seu ambiente local:

    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```

2.  Coloque uma imagem de exemplo (por exemplo, `imagem_exemplo.jpg` ou `imagem_exemplo.png`) no mesmo diretório do script `filtro_imagem.py`.

### Execução

Para rodar o script e aplicar os filtros, execute o arquivo `filtro_imagem.py` a partir do terminal:

```bash
python filtro_imagem.py
```

### Escolhendo e Configurando Filtros

Dentro do arquivo `filtro_imagem.py`, na seção `if __name__ == "__main__":`, você encontrará os kernels de filtro pré-definidos e uma seção para escolher qual filtro aplicar. Descomente apenas o bloco correspondente ao filtro que deseja testar:

```python
    # --- Escolha qual filtro aplicar ---
    print("\nEscolhendo o filtro...")
    
    # Descomente apenas um dos blocos abaixo para escolher o filtro:

    filter_kernel = blur_kernel
    filter_name = "Desfoque_Box"

    # filter_kernel = edge_kernel
    # filter_name = "Detecção_de_Bordas_Laplaciano"

    # filter_kernel = sharpen_kernel
    # filter_name = "Nitidez"
    
    # filter_kernel = emboss_kernel
    # filter_name = "Relevo_Emboss"
```

-----

## 🖼️ Exemplos de Saída

Ao executar o script, ele salvará a imagem original (convertida para o formato interno) e a imagem filtrada no mesmo diretório, com nomes como `original_image_color.png` e `filtered_image_Desfoque_Box.png` (o nome do arquivo filtrado varia de acordo com o filtro aplicado).

Você pode comparar visualmente o antes e depois da aplicação de cada filtro.

-----

## 👥 Créditos

Este projeto foi desenvolvido por:

  * **[Pedro Augusto Gonçalves Lucena]** (lucena.pedro@academico.ifpb.edu.br])
  * **[Maria Clara Colaço Da Costa ]** ([clara.colaco@academico.ifpb.edu.br])
  * **[Sophia Sales Fernades]** ([sophia.sales@academico.ifpb.edu.br])


**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia da Paraíba (IFPB) - Campus Campina Grande
**Disciplina:** Álgebra Linear

-----

**Nota:** Este projeto é para fins educacionais, demonstrando os princípios básicos de Álgebra Linear em processamento de imagens.

-----

