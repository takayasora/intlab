from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import os
import datetime


class sapnet():
    @staticmethod
    def array4DataFrame(array):
        print("DEBUG : (0/8)Converting array to DataFrame")  # トレース情報：配列からデータフレームへの変換開始
        # 行番号を付与して各行の一番目に追加
        for i, row in enumerate(array, start=1):
            row[0] = f"{row[0]}_{i}"

        # Columnの一行目を取得し、ヘッダーとして再利用する
        header_list = ["name"]
        for i in range(len(array)):
            header_list.append(array[i][0])
        df = pd.DataFrame(array, columns=header_list)
        
        return df
    
    @staticmethod
    def DataFrame4array(df):
        print("DEBUG : (0/8)Generating dataframe for array.")
        array = []
        for index, row in df.iterrows():
            data_row = [row['name']] + row.iloc[1:].tolist()
            array.append(data_row)
        return array

    
    @staticmethod
    def example_data():
        print("DEBUG : (0/8)Generating dataframe for array.")
        data = [["knowledge", 0, 0.1, 0, 0.4, 0, 0.3, 0.5],
                ["knowledge", 0.1, 0, 0.4, 0, 0.6, 0, 0],
                ["knowledge", 0, 0.4, 0, 0.2, 0, 0, 0.7],
                ["knowledge", 0.4, 0, 0.2, 0, 0.1, 0, 0],
                ["knowledge", 0, 0.6, 0, 0.1, 0, 0.4, 0.2],
                ["knowledge", 0.3, 0, 0, 0, 0.4, 0, 0.6],
                ["knowledge", 0.5, 0, 0.7, 0, 0.2, 0.6, 0]]

        return data

    @staticmethod
    def example_dataframe():
        print("DEBUG : (0/8)Generating dataframe for dataframe.")
        data = [["knowledge", 0, 0.1, 0, 0.4, 0, 0.3, 0.5],
                ["knowledge", 0.1, 0, 0.4, 0, 0.6, 0, 0],
                ["knowledge", 0, 0.4, 0, 0.2, 0, 0, 0.7],
                ["knowledge", 0.4, 0, 0.2, 0, 0.1, 0, 0],
                ["knowledge", 0, 0.6, 0, 0.1, 0, 0.4, 0.2],
                ["knowledge", 0.3, 0, 0, 0, 0.4, 0, 0.6],
                ["knowledge", 0.5, 0, 0.7, 0, 0.2, 0.6, 0]]

        df = sapnet.array4DataFrame(data)
        
        return df
    
    @staticmethod
    # 拡散する先をソートして返します。
    def next_Allpair(df,stimulus):#sapnetモジュール内で使用
        print("DEBUG : (2/8)Calculating next_Allpair")
        diffusion_list = []
        column = df.iloc[:, stimulus]
        for i in range(len(column)):
            distance_value = column[i]
            if distance_value > 0:# 距離を持たないものを飛ばす（つながってないもの）
                if stimulus == i+1: # 刺激値とi+1が同じ（活性値を保持する部分）は飛ばす
                    continue
                #print(stimulus,i+1)
                diffusion_list.append([distance_value,stimulus,i+1])
                # 配列を一番前の少数を基準にソート
                sorted_diffusion_list = sorted(diffusion_list, key=lambda x: x[0])
                #print(sorted_diffusion_list)
                # 今回の拡散が行われるリスト
                pair_list = [sublist[1:] for sublist in sorted_diffusion_list]
                #print(pair_list)
                # 次のパス一覧を返却
                path_list = [sublist[1:] for sublist in pair_list]
                next_list = [[sublist[0] for sublist in path_list]]
        print("DEBUG : (2/8)Calculating next_Allpair",pair_list)
        return pair_list

    @staticmethod
    def already_pair_remove(pair_list,already_list):#sapnetモジュール内で使用
        return_list = []
        for pair_temp in pair_list:
            if pair_temp not in already_list:
                return_list.append(pair_temp)
                already_list.append(pair_temp)
                reversed_pair = pair_temp[::-1]
                already_list.append(reversed_pair)
                print("DEBUG : (3/8)Removing already pairs",pair_temp,reversed_pair)
            else:
                None
        return return_list,already_list

    
    @staticmethod
    def path_count(df, stimulus):
        print("DEBUG : (5/8)Counting paths for stimulus", stimulus)
        column_name = df.columns[stimulus]  # 指定された数値から列名を取得
        selected_row = df.iloc[stimulus - 1]  # 指定された行を選択
        # print(column_name)
        # print(selected_row)
        # 行の名前と同じ行の数値以外を取得
        row_values = selected_row.drop(index=column_name)
        # print(row_values)
        # 0.0より大きい数値のカウントを追加
        count_above_0 = 0
        for value in row_values[1:]:
            if value > 0.0:
                count_above_0 += 1
        # print("0.0より大きい数値の個数:", count_above_0)
        print("DEBUG : (5/8)Counting paths for stimulus", stimulus,"-->",count_above_0)

        return count_above_0


    @staticmethod
    def path_weight(df, stimulus,receive):
        print("DEBUG : (6/8)Calculating path weight for stimulus", stimulus, "and receive", receive)
        row_number = stimulus-1# 例として2を指定
        column_number = receive
        if stimulus != receive:
            weight = df.iloc[row_number,column_number]
            print("DEBUG : (6/8)Calculating path weight for stimulus", stimulus, "->", receive,"-->",weight)
            return weight


    @staticmethod
    #データフレームを渡すとsapnetのアルゴリズムに基づいてペアとなるリストを返します。
    def stimulus_pairlist(df,stimulus):
        print("INFO  : (1/8)Generating stimulus pair list for stimulus", stimulus)
        already_list=[]
        temp_list = [stimulus]
        path_num_list = []
        path_weight_list = []
        return_pairlist = []
        #print("temp",temp_list)
        while len(temp_list)!=0:
            #print(i)
            now_list = temp_list
            temp_list = []
            for item in range(len(now_list)):
                #print("item",now_list[item])
                pair_list = sapnet.next_Allpair(df,now_list[item])
                #print("pair",pair_list)
                check_pair_list,already_list = sapnet.already_pair_remove(pair_list,already_list)
                #print("al",already_list)
                #print("check",check_pair_list)
                path_list = [sublist[1:] for sublist in check_pair_list]
                next_list = [sublist[0] for sublist in path_list]
                # print("next",next_list)
                temp_list.extend(next_list)
                # print("check",temp_list)
                for active_pair in check_pair_list:
                    ## print(active_pair)
                    return_pairlist.append(active_pair)
                    # 計算部分
                    # offer_num,receive_num = active_pair[0],active_pair[1]
                    # N = sapnet.path_num_calc(df,offer_num)
                    # path_num_list.append(N)
                    # #print(N)
                    # w = sapnet.path_weight_calc(df,offer_num,receive_num)
                    # path_weight_list.append(w)
                    # #print(w)
        print("INFO  : (3/8)Generating stimulus pair list", return_pairlist)
        return return_pairlist
    
    @staticmethod
    def stimulus_add_value(path_quantity,path_weight,last_list,pairA,pairB):
        print("DEBUG : (7/8)calculation stimulus value for pairA(", pairA, ")and pairB(", pairB,")")
        print("DEBUG : (7/8)Lastlist before update:", last_list)  # 更新前のラストリストを表示
        last_value = last_list[pairA-1]
        print("DEBUG : (7/8)pickup last value pair(",pairA,"):", last_value)  # 更新前のラストリストを表示
        N = path_quantity
        w = path_weight
        v = (1/N)*last_value*math.exp(-w)
        print("DEBUG : (7/8)Calculation -> 1/", N, "*", last_value, " * exp(-", w, ")")
        print("DEBUG : (7/8)Calculation -> ",v)
        last_list[pairB-1] = v
        print("DEBUG : (7/8)Lastlist after update:", last_list)  # 更新後のラストリストを表示
        return v,last_list
    
    @staticmethod
    def last_dataframe_setting(df,stimulus,first_stimulus_value):
        # 元のデータフレームの長さを取得
        length = len(df)
        last_list=[]
        # 0の列を指定された数だけ追加
        for i in range(length):
            if i == stimulus-1:
                last_list.append(first_stimulus_value)  # 新しい列を追加し、指定された列に1を設定
                df.iloc[i, i+1] += first_stimulus_value
            else:
                last_list.append(0)  # それ以外の列は0を設定
        print("DEBUG : (4/8)Creating last dataframe for stimulus", stimulus,"->",last_list)
        return last_list

    @staticmethod
    def df_update(df,stimulus_value,pairA,pairB):
        print("DEBUG : (8/8)Updating DataFrame")  # デバッグ情報：データフレームの更新開始
        # 数値で行と列を指定して値に1を加算
        row_index = pairB  # 行のインデックス (0から始まる)
        col_index = pairB  # 列のインデックス (0から始まる)
        print("DEBUG : (8/8)moved from ",pairA," to ",pairB,", adding ",stimulus_value,".")
        df.iloc[row_index-1, col_index] += stimulus_value
        print("DEBUG : (8/8)DataFrame update completed")  # デバッグ情報：データフレームの更新が完了

        return df
    
    @staticmethod
    def stimulus_calc(df,stimulus,first_stimulus_value):
        print("\033[31mINFO  : Sapnet's algorithm, Start the calculations.\033[0m")  # ANSIエスケープコードを使って赤文字に設定
        pair_list = sapnet.stimulus_pairlist(df,stimulus)
        last_list = sapnet.last_dataframe_setting(df,stimulus,first_stimulus_value)
        folder_name,Heatmap_path,Network_path,Plotpoint_path,GIF_source_path,GIF_100_path,GIF_1000_path = sapnet.makeup_folder()

        for pair in pair_list:
            paths = sapnet.path_count(df,pair[0])
            weight = sapnet.path_weight(df,pair[0],pair[1])
            stimulus_value,last_list = sapnet.stimulus_add_value(paths,weight,last_list,pair[0],pair[1])
            sapnet.graph_show(df,GIF_source_path)
            df = sapnet.df_update(df,stimulus_value,pair[0],pair[1])
        
        sapnet.graph_show(df,GIF_source_path)
        sapnet.create_gif(GIF_source_path,GIF_100_path)
        return df
    
    @staticmethod
    def graph_show(df,GIF_source_path):
        diagonal_matrix = np.diag(df.iloc[:, 1:].values)
        plt.bar(np.arange(len(diagonal_matrix)) + 1, diagonal_matrix, color='b')
        plt.title('Stimulus_value')
        plt.xlabel('Knowledge')
        plt.ylabel('Values')
        
        # 指定したフォルダ内のファイルをリスト
        files = os.listdir(GIF_source_path)

        # PNGファイルの数をカウント
        png_count = sum(1 for file in files if file.lower().endswith(".png"))

        # フォーマットされたファイル名を生成
        image_filename = os.path.join(GIF_source_path, f"gif_source_{png_count+1:03d}")

        print(GIF_source_path)
        print(image_filename)
        if GIF_source_path:
            plt.savefig(image_filename)
            plt.close()
        else:
            plt.show()

    @staticmethod
    def create_gif(GIF_source_path, GIF_100_path):
        # GIF用の画像ファイルリストを取得
        image_list = sorted([os.path.join(GIF_source_path, file) for file in os.listdir(GIF_source_path) if file.lower().endswith(".png")])

        # 画像リストが存在しない場合は処理を中止
        if not image_list:
            print("No image files found in the source path.")
            return

        # GIFファイルの保存先
        gif_filename = GIF_100_path

        # 画像を開いてリストに格納
        images = [Image.open(img) for img in image_list]

        # GIFファイルを生成
        images[0].save(gif_filename, save_all=True, append_images=images[1:], duration=100, loop=0)


    @staticmethod
    def attenuation(df,attenuation_percentage):
        # 少数で指定された数値分削る関数
        # 元のデータフレームの長さを取得
        length = len(df)
        # 0の列を指定された数だけ追加
        for i in range(length):
            df.iloc[i, i+1] *= (1-attenuation_percentage)
        return df
    
    @staticmethod
    def makeup_folder():
        # 現在時刻を取得
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        # 現在時刻を使用することでアウトプットファルダを重複なく作成することができる
        folder_name = f"./Output_{current_time}"
        # if not os.path.exists(folder_name):
        #     os.makedirs(folder_name)
        
        # 現在時刻を使用することでアウトプットファルダを重複なく作成することができる
        gif_folder_name = folder_name+"/GIF_source/"
        if not os.path.exists(gif_folder_name):
            os.makedirs(gif_folder_name)

        Heatmap_path = folder_name + '/heatmap.png'
        Network_path = folder_name + '/network.png'
        Plotpoint_path = folder_name + '/plotpoint.png'
        GIF_source_path = gif_folder_name
        GIF_100_path = folder_name + '/graph_100.gif'
        GIF_1000_path = folder_name + '/graph_1000.gif'

        return folder_name,Heatmap_path,Network_path,Plotpoint_path,GIF_source_path,GIF_100_path,GIF_1000_path

    # @staticmethod
    # def outputlog(folder_name):
    #     # 出力
        

    