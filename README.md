# 句子相似度計算

這個專案提供了一個簡單的方法來計算兩個句子之間的相似度。 支持兩種方法：BERT 和 FastText。

## 安裝

首先，需要安裝以下依賴項：

```bash
pip install fasttext
pip install sentence-transformers
pip install scikit-learn
```

## 使用方法

1. 下載預訓練的 FastText 中文模型（只需下載一次）：

```bash
python sentence_similarity.py
```

2. 使用命令行界面計算句子的相似度：

```bash
python sentence_similarity.py "妳喜歡哪一種顏色" "妳最喜歡的顏色是什麼呢"
```

您可以選擇使用 `--method` 參數來切換方法，選擇 'bert' 或 'fasttext'。

```bash
python sentence_similarity.py "妳喜歡哪一種顏色" "妳最喜歡的顏色是什麼呢" --method bert
```

## 範例

輸入：

```bash
python sentence_similarity.py "妳喜歡哪一種顏色" "妳最喜歡的顏色是什麼呢"
```

輸出：

```
句子1: 妳喜歡哪一種顏色
句子2: 妳最喜歡的顏色是什麼呢
相似度: 90.870 %
執行時間: 0.822 秒
```

## 貢獻

如果您想為這個專案做出貢獻，請在提交拉取請求之前先開一個問題，以便我們可以討論您的建議。

## 許可

本專案採用 MIT 許可證。