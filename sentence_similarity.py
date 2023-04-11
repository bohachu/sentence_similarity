import argparse
import time

import fasttext
import fasttext.util
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

fasttext.util.download_model('zh', if_exists='ignore')
ft = fasttext.load_model('cc.zh.300.bin')


def similarity_percent(s1, s2, method="bert"):
    print("句子1:", s1)
    print("句子2:", s2)

    if method == "bert":
        model = SentenceTransformer("paraphrase-distilroberta-base-v1")
        sentence_embeddings1 = model.encode([s1])
        sentence_embeddings2 = model.encode([s2])
    elif method == "fasttext":
        model = fasttext.load_model("cc.zh.300.bin")  # 使用適當的預訓練模型
        sentence_embeddings1 = [model.get_sentence_vector(s1)]
        sentence_embeddings2 = [model.get_sentence_vector(s2)]
    else:
        raise ValueError("Invalid method. Please choose 'bert' or 'fasttext'.")

    similarity_score = cosine_similarity(sentence_embeddings1, sentence_embeddings2)[0][0]
    similarity_percent = round(similarity_score * 100, 2)

    return similarity_percent


def main():
    parser = argparse.ArgumentParser(description="計算兩個句子的相似度")
    parser.add_argument("sentence1", type=str, default="妳喜歡哪一種顏色", nargs="?", help="妳喜歡哪一種顏色")
    parser.add_argument("sentence2", type=str, default="妳最喜歡的顏色是什麼呢", nargs="?", help="妳最喜歡的顏色是什麼呢")
    parser.add_argument("--method", type=str, default="fasttext", choices=["bert", "fasttext"],
                        help="選擇使用的方法：'bert' 或 'fasttext'")

    args = parser.parse_args()

    t = time.time()
    similarity = similarity_percent(args.sentence1, args.sentence2, args.method)
    print(f"相似度: {similarity:.3f} %")
    print(f"執行時間: {time.time() - t:.3f} 秒")


if __name__ == "__main__":
    main()
