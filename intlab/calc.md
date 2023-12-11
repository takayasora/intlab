# SAP-netの計算

このプログラムでは、`sapnet` クラスが定義されており、その中にさまざまなメソッドが含まれています。与えられたデータフレーム (`df`) に対して、`stimulus_calc` メソッドが拡散計算を行います。以下に、プログラムを呼び出した際の主な結果と計算式を示します。

```python
# プログラム呼び出し
getdatas = [1, 2, 4, 8, 16, 32, 64, 128]
message = ''

for getdata in getdatas:
    line_data = []
    for j in range(1):
        df = sapnet.example_dataframe()

        for i in range(getdata):
            df = sapnet.stimulus_calc(df=df, stimulus=random.randint(1, len(df)))
            diagonal_matrix = np.diag(df.iloc[:, 1:].values)
        line_data.append(diagonal_matrix)

    transposed_line_data = np.transpose(line_data)
    averaged_lists = [np.mean(transposed_row) for transposed_row in transposed_line_data]
    overall_average = np.mean(averaged_lists)
    add_message = "{},{}".format(averaged_lists, overall_average)
    message = message + '\n' + add_message

print(message)
```

`stimulus_calc` メソッドでは、与えられたデータフレーム (`df`) に対してランダムな刺激 (`stimulus`) を与え、その拡散を計算します。その結果、拡散が行われた後のデータフレームが返されます。

計算式は主に `stimulus_add_value` メソッド内で行われています。このメソッドでは、拡散される対象となるペアの情報（`pairA` と `pairB`）およびそれに関連するパスの数と重みを使用して、活性値の計算が行われています。具体的な計算式は以下の通りです：


$$ v = \frac{1}{N} \cdot \text{{last\_value}} \cdot e^{-w} \$$


ここで、**N** は `paths` として `path_count` メソッドで計算されたパス（活性値が伝播する経路）の数、`last_value` は前回の活性値、**w** は `weight` として `path_weight` メソッドで計算された経路の重みです。

また、last_valueは前回の拡散値の値を用いる。また、初回はハイパーパラメータによって、指定できる。


上記のように、`stimulus_calc`メソッドで、計算された `v` は次の計算に用いる、`last_list` に更新されます。これらの値が次の拡散計算に使用されます。


# 減衰関数の必要性

実験プログラム全体の流れを簡単に説明すると、以下のようになります：

1. ランダムなノードに対して拡散計算（100回繰り返す）。
2. 各拡散計算結果を `diagonal_matrix` として取得。
3. `diagonal_matrix` から平均リスト `averaged_lists` を取得（10回繰り返す）。
4. 各 `diagonal_matrix` における平均活性値の平均を `overall_average` として計算。
5. `overall_average` を出力。

`v` の具体的な値は、各拡散計算において `stimulus_add_value` メソッド内で計算され、その平均が `overall_average` に影響を与えます。


`overall_average` の計算式は、各拡散計算において得られる平均活性値の平均です。それを数学的に表現すると以下のようになります：

$$
\text{{overall\_average}} = \frac{1}{M} \sum_{i=1}^{M} \left( \frac{1}{N} \sum_{j=1}^{N} \text{{last\_value}}_j^{(i)} \cdot e^{-w_j^{(i)}} \right)
$$

ここで、(M) は外側のループである拡散計算を行う回数（例では10回）、(N) は内側のループである各拡散計算において得られるパスの数、
$$ \text{{last\_value}}_j^{(i)} $$
および 
$$ w_j^{(i)} $$

 はそれぞれ (j)-番目のパスにおける前回の活性値と重みです。

この式は、各拡散計算において得られる平均活性値（`averaged_lists`）と、その平均を求めています。

その結果は下記のようになりました。

![img](https://gyazo.com/0e5a15af30ed2e8a696618ed0af3ede8.png)


当然、拡散回数が増えると活性値が増えていった。今回はその増えていく様子に注目したい。
知識の選択回数が増えていくたびに、知識間の値のブレが大きく見えることがわかる。
よって、知識の活性値の増加に分散があることがわかる。分散を可視化すると下記の通りになる。

![img](https://gyazo.com/81400fb887d0c976b15570385a2d6eaa.png)

よって、拡散を実施するたびに、同じ知識が選択される可能性が高くなっていることを示している。
選択された知識が選ばれやすくなることはあってもよいと考えるが、それだけを選べばよいということではない。
そのため、適度な回数の活性化が行われた際に、人間の忘却に当たる減衰関数を実装する。

また、減衰関数は、知識選択の平等性を保つことを目的とする。
