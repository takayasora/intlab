from PIL import Image
import os

def convert_images_to_pdf(input_folder_path, output_folder_path):
    # サポートする画像ファイルの拡張子
    supported_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', '.webp')
    
    for root, dirs, files in os.walk(input_folder_path):
        for file in files:
            if file.lower().endswith(supported_extensions):
                image_path = os.path.join(root, file)
                pdf_file_name = os.path.splitext(file)[0] + '.pdf'
                pdf_path = os.path.join(output_folder_path, pdf_file_name)
                
                # すでにPDFが存在する場合はスキップ
                if not os.path.exists(pdf_path):
                    try:
                        # 画像を開いてPDFに変換
                        with Image.open(image_path) as img:
                            # アルファチャネル（透明度）を持つ画像を処理
                            if img.mode == 'RGBA' or img.mode == 'LA':
                                img = img.convert('RGB')
                            img.save(pdf_path, "PDF", resolution=100.0)
                            print(f"Converted {image_path} to {pdf_path}")
                    except Exception as e:
                        print(f"Error converting {image_path}: {e}")
                else:
                    print(f"PDF already exists for {image_path}, skipping.")

# 入力フォルダと出力フォルダを指定して関数を呼び出す
input_folder_path = './image/'
output_folder_path = './'
convert_images_to_pdf(input_folder_path, output_folder_path)
