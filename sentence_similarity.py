import argparse
import time

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def simularity_percent(s1, s2):
    print("句子1:", s1)
    print("句子2:", s2)
    model = SentenceTransformer('paraphrase-distilroberta-base-v1')
    sentence_embeddings1 = model.encode([s1])
    sentence_embeddings2 = model.encode([s2])
    similarity_score = cosine_similarity(sentence_embeddings1, sentence_embeddings2)[0][0]
    similarity_percent = round(similarity_score * 100, 2)

    return similarity_percent


def main():
    parser = argparse.ArgumentParser(description="計算兩個句子的相似度")
    parser.add_argument("sentence1", type=str, default="妳喜歡哪一種顏色", nargs="?", help="妳喜歡哪一種顏色")
    parser.add_argument("sentence2", type=str, default="妳最喜歡的顏色是什麼呢", nargs="?", help="妳最喜歡的顏色是什麼呢")

    args = parser.parse_args()

    t = time.time()
    similarity = simularity_percent(args.sentence1, args.sentence2)
    print(f"相似度: {similarity:.3f} %")
    print(f"執行時間: {time.time() - t:.3f} 秒")


if __name__ == "__main__":
    main()
