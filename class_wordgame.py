import json
import random
import time

from deep_translator import GoogleTranslator
from pygame import mixer


class WordGame:
    def __init__(self):
        self.word_file = "data/word.txt"
        self.translation_file = "data/word_meanings.json"
        self.score_file = "word_game_score.csv"

        self.words = []
        self.meanings = {}
        self.correct_count = 0
        self.elapsed_time = 0

        self.translator = GoogleTranslator(source="en", target="ko")
        mixer.init()

    def word_load(self):
        with open(self.word_file, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip()

                if word:
                    self.words.append(word)

    def load_meanings(self):
        try:
            with open(self.translation_file, "r", encoding="utf-8") as f:
                self.meanings = json.load(f)

        except FileNotFoundError:
            self.meanings = {}

    def get_meaning(self, word):
        if word in self.meanings:
            return self.meanings[word]

        try:
            meaning = self.translator.translate(word)
            self.meanings[word] = meaning

            with open(self.translation_file, "w", encoding="utf-8") as f:
                json.dump(self.meanings, f, ensure_ascii=False, indent=2)

            return meaning

        except Exception:
            return "번역을 가져오지 못했습니다."

    def play_sound(self, file_path):
        mixer.music.load(file_path)
        mixer.music.play()

    def game_run(self):
        start_time = time.time()

        for turn in range(1, 6):
            question = random.choice(self.words)

            print(f"\n[{turn}/5] 제시 단어: {question}")
            answer = input("입력: ").strip()

            if answer == question:
                print("정답")
                self.play_sound("assets/good.wav")
                self.correct_count += 1
            else:
                print("오답")
                self.play_sound("assets/bad.wav")

            print(f"뜻: {self.get_meaning(question)}")

        self.elapsed_time = time.time() - start_time

    def score_print(self):
        print("\n게임 종료")
        print(f"맞힌 개수: {self.correct_count}")
        print(f"걸린 시간: {self.elapsed_time:}초")

        if self.correct_count >= 3:
            print("합격")
        else:
            print("불합격")

    def save_result(self):
        with open(self.score_file, "a", encoding="utf-8") as f:
            f.write(f"{self.elapsed_time:},{self.correct_count}\n")

    def run(self):
        self.word_load()
        self.load_meanings()
        self.game_run()
        self.score_print()
        self.save_result()


if __name__ == "__main__":
    game = WordGame()
    game.run()
