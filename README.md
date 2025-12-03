Based on the repository files and their Python code for digital image processing exercises, here's an enhanced README description:

````markdown name=README.md
## Processamento de Imagem - PDI 2025-2
### Professor João Miguel

Este repositório contém exemplos, exercícios e demonstrações do curso "Processamento de Imagens 2025-2", ministrado na Faculdade SENAI por Prof. João Miguel. Os códigos utilizam Python e as bibliotecas Pillow (PIL) e Tkinter, baseando-se no livro "Raspberry Pi Image Processing Programming".

### Conteúdo

Os scripts estão organizados em capítulos, demonstrando conceitos fundamentais de processamento digital de imagens:

- **Leitura e Exibição de Imagens**: 
  - Carregamento de imagens com Pillow.
  - Exibição básica usando `.show()` ou interfaces gráficas com Tkinter.

- **Propriedades de Imagens**:
  - Visualização do modo, formato, tamanho e bandas.
  - Extração de informações dos metadados das imagens.

- **Manipulação de Canais de Cor**:
  - Separação de canais (R, G, B).
  - Mesclagem de imagens utilizando o método `merge()`.

- **Conversão de Espaços de Cores**:
  - Exemplos de conversão RGB ➔ L (luminância).
  - Análise comparativa entre modos de cores e tamanhos em bytes.

- **Blend/Ajuste de Transparência entre Imagens**:
  - Demonstração de mistura de duas imagens pelo parâmetro alpha, com controle via interface gráfica.

- **Redimensionamento**:
  - Alteração dinâmica da resolução da imagem usando o método `resize()`.

- **Rotação e Transposição Geométrica**:
  - Rotação por qualquer ângulo (`rotate()`).
  - Reflexão vertical/horizontal e rotações múltiplas de 90°, usando `transpose()`.

### Execução

Os scripts foram desenvolvidos para rodar em ambientes Python compatíveis com as bibliotecas **Pillow** e **Tkinter**. Certifique-se de possuir as imagens na pasta indicada nos scripts, ou adapte o caminho conforme necessidade.

### Exemplos

- Demonstração de visualização simples: 
  - `chapter03/ch3_prog01.py`
- Exibição e manipulação de canais e cores: 
  - `chapter04/ch4_prog01.py`, `chapter04/ch4_prog01_gemini.py`
- Blending com ajuste dinâmico de alpha:
  - `chapter04/ch4_prog03.py`, `chapter04/ch4_prog03_gemini.py`
- Redimensionamento e rotação interativos:
  - `chapter04/ch4_prog04.py`, `chapter04/ch4_prog04_gemini.py`, `chapter04/ch4_prog05.py`
- Transformações geométricas (espelhos, rotações): 
  - `chapter04/ch4_prog06.py`, `chapter04/ch4_prog06_gemini.py`, `chapter04/ch4_prog06_geminiv2.py`

### Referências

- Livro: *Raspberry Pi Image Processing Programming*
- Base de imagens: https://sipi.usc.edu/database/database.php?volume=misc

---

Sinta-se livre para explorar os exemplos, adaptar os scripts e contribuir com melhorias!
````
