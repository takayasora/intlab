from PIL import Image
import os
from reportlab.pdfgen import canvas

def convert_images_to_pdf(folder_path):
    # 指定フォルダ内のすべてのjpg, png, gifファイルを探す
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.png', '.gif')):
                image_path = os.path.join(root, file)
                pdf_path = image_path.rsplit('.', 1)[0] + '.pdf'
                
                # すでにPDFが存在する場合はスキップ
                if not os.path.exists(pdf_path):
                    try:
                        # 画像を開いてPDFに変換
                        with Image.open(image_path) as img:
                            # アルファチャネル（透明度）を持つ画像を処理
                            if img.mode == 'RGBA':
                                img = img.convert('RGB')
                            img.save(pdf_path, "PDF", resolution=100.0)
                            print(f"Converted {image_path} to {pdf_path}")
                    except Exception as e:
                        print(f"Error converting {image_path}: {e}")
                else:
                    print(f"PDF already exists for {image_path}, skipping.")

# フォルダパスを指定して関数を呼び出す
folder_path = './image/'
convert_images_to_pdf(folder_path)
