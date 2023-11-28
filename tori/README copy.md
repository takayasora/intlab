# intlab

Membar List
| Kono Hitoshi                                                                                                                            | Takaya Sora                                                                                                                                           | Toriyabe Yuki                                                                                                                    | Suga Kanato                                                                                                                    | Kobayashi Mizuki                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| ![Image 1](URL_to_image_1)              | ![Image 2](URL_to_image_2)                                  | ![Image 3](URL_to_image_3)                                                                                                 | ![Image 4](URL_to_image_4)                                                                                                 | ![Image 5](URL_to_image_5)                                                                                                 |




| YouTube 128×128                                                                                                                            | Twitter 128×128                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![youtube_social_square_red.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/362315/65d2d650-aee5-40cb-2093-607d931ec087.png) | ![Twitter_Social_Icon_Square_Colorのコピー.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/362315/7a000ef8-21c1-1e86-2942-f1933ffe839b.png) |


<h1 align="center">
<a href="https://takayasora.com">
  <img src="../base/source/welcome.gif" alt="Sora's GitHub Banner" width="1280">
</a>
</h1>
</br>


[![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](
https://numfocus.org)
[![PyPI Downloads](https://img.shields.io/pypi/dm/numpy.svg?label=PyPI%20downloads)](
https://pypi.org/project/numpy/)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/numpy.svg?label=Conda%20downloads)](
https://anaconda.org/conda-forge/numpy)
[![Stack Overflow](https://img.shields.io/badge/stackoverflow-Ask%20questions-blue.svg)](
https://stackoverflow.com/questions/tagged/numpy)
[![Nature Paper](https://img.shields.io/badge/DOI-10.1038%2Fs41586--020--2649--2-blue)](
https://doi.org/10.1038/s41586-020-2649-2)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/numpy/numpy/badge)](https://api.securityscorecards.dev/projects/github.com/numpy/numpy)

## 概要
intlabとは、東京電機大学 知能情報システム研究室が開発したPythonを使用した機械学習サポート用のパッケージ群です

- **Website:** https://takayasora.github.io/intlab/
- **Documentation:** https://takayasora.github.io/intlab/4-BUILD_INSTALL.html
- **Mailing list:** https://mail.python.org/mailman/listinfo/numpy-discussion
- **Source code:** https://github.com/takayasora/intlab
- **Bug reports:** https://github.com/takayasora/intlab/issue

## パッケージ
- sapnet
- and more...
  
## 使用バージョン
sapnetは以下のパッケージを用いて作成しています
- pillow 9.5.0
- matplotlib 3.7.1
- pandas 2.0.0
- numpy 1.23.5
- seaborn 0.12.2
- japanize-matplotlib 1.1.3
- networkx 3.1

## sapnetの導入テスト
sapnetは以下のコードを実行することでテストすることができます

```Python
import intlab

sapnet = intlab.sapnet

df = sapnet.stimulus_calc()
```

## ライセンス
  大学の卒業研究で作成したパッケージの明確な[ライセンス情報](https://takayasora.github.io/intlab/6-LICENSE.html)を提供する

<!--
NumPy is a community-driven open source project developed by a diverse group of
[contributors](https://numpy.org/teams/). The NumPy leadership has made a strong
commitment to creating an open, inclusive, and positive community. Please read the
[NumPy Code of Conduct](https://numpy.org/code-of-conduct/) for guidance on how to interact
with others in a way that makes our community thrive.
-->