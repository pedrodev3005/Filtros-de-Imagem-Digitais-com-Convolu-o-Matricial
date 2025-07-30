import numpy as np
from PIL import Image



def apply_convolution(image_array, kernel):
    """
    Aplica a operação de convolução em uma imagem (suporta tons de cinza ou RGB).

    Args:
        image_array (np.array): A imagem como um array NumPy (2D para tons de cinza, 3D para RGB).
        kernel (np.array): O kernel (máscara) do filtro.

    Returns:
        np.array: A imagem resultante após a convolução.
    """
    if image_array.ndim == 2:  # Imagem em tons de cinza (2D)
        image_height, image_width = image_array.shape
        is_color = False
        num_channels = 1
        processed_channels = [image_array]
    elif image_array.ndim == 3:  # Imagem colorida (RGB - 3D)
        image_height, image_width, num_channels = image_array.shape
        is_color = True
        # Dividir a imagem em canais individuais para processamento
        processed_channels = [image_array[:, :, c] for c in range(num_channels)]
    else:
        raise ValueError("Formato de imagem não suportado. Esperado 2D (grayscale) ou 3D (RGB).")

    kernel_height, kernel_width = kernel.shape
    pad_h = kernel_height // 2
    pad_w = kernel_width // 2

    output_channels = []

    for channel_array in processed_channels:
        padded_channel = np.pad(channel_array, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
        output_channel = np.zeros_like(channel_array, dtype=float)

        for i in range(image_height):
            for j in range(image_width):
                window = padded_channel[i:i + kernel_height, j:j + kernel_width]
                output_channel[i, j] = np.sum(window * kernel)

        output_channels.append(output_channel)

    # Recombinar os canais
    if is_color:
        # Empilhar os canais de volta para formar uma imagem RGB 3D
        output_image = np.stack(output_channels, axis=-1)
    else:
        output_image = output_channels[0]  # Se for grayscale, retorna o único canal

    # Normalizar e clipar os valores para garantir que estejam no intervalo de 0-255
    output_image = np.clip(output_image, 0, 255)
    return output_image.astype(np.uint8)



if __name__ == "__main__":
    # 1. Carregar uma imagem de exemplo
    # Substitua 'imagem_exemplo.jpg' pelo caminho para uma imagem que você tenha
    try:
        img_path = 'imagem_exemplo.png'  # Crie ou baixe uma imagem e renomeie
        original_image = Image.open(img_path)
        original_image_array = np.array(original_image)
        print(f"Imagem original carregada. Dimensões: {original_image_array.shape}")
    except FileNotFoundError:
        print(f"Erro: A imagem '{img_path}' não foi encontrada.")
        print("Por favor, certifique-se de ter uma imagem no mesmo diretório do script ou forneça o caminho completo.")
        exit()

    # 2. Definir Kernels para diferentes filtros

    # Kernel de Desfoque (Box Blur)
    # A soma dos elementos é 1 para não alterar o brilho geral da imagem.
    # Exemplo de 3x3:
    blur_kernel = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ], dtype=float) / 9.0

    # Exemplo de 5x5 para MAIS desfoque Box:
    # blur_kernel = np.array([
    #     [1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1]
    # ], dtype=float) / 25.0

    # Kernel de Detecção de Bordas (Laplaciano)
    # A soma dos elementos é 0, o que realça as mudanças de intensidade.
    edge_kernel = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ], dtype=float)

    # Kernel de Nitidez (Sharpen)
    sharpen_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ], dtype=float)

    # Kernel Emboss (Relevo)
    emboss_kernel = np.array([
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ], dtype=float)

    # Kernel Outline (Contorno)
    outline_kernel = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ], dtype=float)

    # --- Escolha qual filtro aplicar ---
    print("\nEscolhendo o filtro...")

    # Descomente apenas um dos blocos abaixo para escolher o filtro:

    #filter_kernel = blur_kernel
    #filter_name = "Desfoque_Box"

    #filter_kernel = edge_kernel
    #filter_name = "Detecção_de_Bordas_Laplaciano"

    #filter_kernel = sharpen_kernel
    #filter_name = "Nitidez"

    #filter_kernel = emboss_kernel
    #filter_name = "Relevo_Emboss"

    filter_kernel = outline_kernel
    filter_name = "Contorno_Outline"

    print(f"Aplicando o filtro: {filter_name}")
    print("Kernel:\n", filter_kernel)

    # 3. Aplicar o filtro
    filtered_image_array = apply_convolution(original_image_array, filter_kernel)

    # 4. Exibir as imagens
    filtered_image = Image.fromarray(filtered_image_array)

    # Salvar as imagens
    # A imagem original agora pode ser colorida, então salvamos como 'original_image_color.png'
    original_image.save("original_image_color.png")
    filtered_image.save(f"filtered_image_{filter_name.replace(' ', '_').replace('(', '').replace(')', '')}.png")

    print(
        f"\nImagens salvas como 'original_image_color.png' e 'filtered_image_{filter_name.replace(' ', '_').replace('(', '').replace(')', '')}.png'.")
    print("Você pode abri-las para comparar os resultados.")

    # Para exibir as imagens diretamente, você pode descomentar as linhas abaixo:
    original_image.show(title="Imagem Original Colorida")
    filtered_image.show(title=f"Imagem Filtrada - {filter_name}")