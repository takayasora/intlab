# 機能
  sapnetライブラリの関数を紹介します。

## データ準備
- ```python
    array4DataFrame(array)
  ```
  +  配列をpandasが提供する２次元データのDataFrameに変換し、行番号とヘッダーを追加して返す。
- ```python
    DataFrame4array(df)
  ```
  + DataFrameを配列に変換して返す。
- ```python
    example_data()
  ```
  + ライブラリにて予め設定されている配列データを返す。
- ```python
  example_dataframe()
  ```
  + ライブラリにて予め設定されている配列データをDataFrameにしたものを返す。
## 計算
- ```python
  next_Allpair(df, stimulus)
  ```
  + 指定されたノード番号への刺激に対して、拡散する先の一覧をソートしたペアをリストとして返す。
- ```python
  already_pair_remove(pair_list, already_list)
  ``` 
  + next_Allpair(df, stimulus)にて得たリストから既に存在するペアを除外したリストを返す。
- ```python
  path_count(df, stimulus)
  ```
  + 指定された刺激番号のノードが保持している経路の数をカウントして返す。
- ```python
  path_weight(df, stimulus, receive)
  ```
  + 指定された経路間の重みを返す。
- ```python
  stimulus_pairlist(df, stimulus)
  ```
  + 刺激に対する拡散可能なペアのリストを生成して返す。
- ```python
  stimulus_add_value(path_quantity, path_weight, last_list, pairA, pairB)
  ```
  + 拡散されてきた活性値を基に、拡散する活性値を計算し値の更新を行い、拡散する活性値と更新後のリストを返す。
- ```python
  attenuation(df, attenuation_percentage)
  ```
  + データフレームの対角行列内の活性値を指定した割合で削減する。
- ```python
  stimulus_calc(df=None, stimulus=1, first_stimulus_value=1.0)
  ```
  + サンプルデータを用いて刺激計算を行い、更新されたデータフレームを返す。
- ```python
  last_dataframe_setting(df, stimulus, first_stimulus_value)
  ```
  + 拡散されてきたノード番号を基に、次の拡散先を見つけるための一時保存先を作成
- ```python
  df_update(df, stimulus_value, pairA, pairB)
  ```
  + 更新された活性値を加算したデータフレームを返す。
## ファイル出力
- ```python
  create_graph(df, GIF_source_path, plotpoint_list)
  ```
  + データフレームから対角行列内の活性値のデータを参照し、グラフを作成し、GIFソースパスに保存する。
- ```python
  create_gif(GIF_source_path, GIF_100_path, GIF_1000_path)
  ```
  + GIF用の画像ファイルを生成する。
- ```python
  makeup_folder()
  ```
  + 出力用のフォルダパスと各種ファイルパスを作成して返す。
- ```python
  create_heatmap(df, Heatmap_path)
  ```
  + ヒートマップを作成し、指定されたパスに保存する。
- ```python
  create_network(df, Network_path)
  ```
  + ネットワーク図を作成し、指定されたパスに保存する。
- ```python
  create_plotpoint(plotpoint_list, Plotpoint_path)
  ```
  + 折れ線グラフを作成し、指定されたパスに保存する。
  





