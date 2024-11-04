import fitz
import cv2
def pdf_to_png_and_crop(pdf_path, output_folder, x, y, w, h):

    """Converte um PDF para PNG, recorta uma região específica e salva a imagem.

    Args:
        pdf_path: Caminho completo para o arquivo PDF.
        output_folder: Caminho completo para a pasta de saída.
        x: Coordenada x do canto superior esquerdo da região a ser recortada.
        y: Coordenada y do canto superior esquerdo da região a ser recortada.
        w: Largura da região a ser recortada.
        h: Altura da região a ser recortada.

    """
    # Abre o documento PDF
    doc = fitz.open(pdf_path)

    # Itera sobre cada página do documento
    for page_index in range(len(doc)):
        page = doc[page_index]

        # Renderiza a página como uma imagem pixmap
        pix = page.get_pixmap()

        # Salva a imagem como PNG
        img_path = f"{output_folder}noem_desejado_para_arquivo{page_index}.png"
        pix.save(img_path)

        # Carrega a imagem PNG recém-criada
        img = cv2.imread(img_path)

        # Recorta a imagem
        cropped_img = img[y:y+h, x:x+w]

        # Salva a imagem recortada
        cv2.imwrite(img_path, cropped_img)
# Exemplo de uso
pdf_path = r"caminho_pdf"
output_folder = r"pasta que deseja salvar o png"

# Defina as coordenadas da região a ser recortada
x = 0
y = 0
w = 0
h = 0

pdf_to_png_and_crop(pdf_path, output_folder, x, y, w, h)
