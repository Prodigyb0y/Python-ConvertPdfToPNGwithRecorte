# ✂️ PDF to PNG Cropper

Uma ferramenta eficiente para converter páginas de arquivos PDF em imagens PNG, com funcionalidade integrada de recorte (crop) baseado em coordenadas personalizadas. Ideal para extração de dados visuais, pré-processamento para OCR ou criação de datasets.

## 🚀 Funcionalidades

Este projeto oferece uma solução automatizada para o tratamento de documentos PDF:

* **Conversão PDF para PNG:** Transforma cada página do documento original em um arquivo de imagem isolado de alta qualidade.
* **Recorte de Precisão:** Permite definir uma "Região de Interesse" (ROI) específica para ser mantida na imagem final.
* **Personalização Total:** Ajuste fino das coordenadas (`x`, `y`) e dimensões (`largura`, `altura`) da área de recorte.
* **Nomeação Organizada:** Os arquivos de saída são salvos com nomenclatura padronizada, incluindo o índice da página para fácil ordenação.

## 🛠️ Pré-requisitos

Para executar este projeto, você precisará das seguintes dependências:

*(Nota: Liste aqui as bibliotecas necessárias. Exemplo comum em Python:)*
* Python 3.8+
* pdf2image
* Pillow (PIL)
* Poppler (dependência de sistema para pdf2image)

```bash
pip install pdf2image Pillow
