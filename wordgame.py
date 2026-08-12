import json
from deep_translator import GoogleTranslator
from pygame import mixer
import random
import time
mixer.init()

def wordLoad():
    words = []

    with open('data/word.txt','r',encoding='utf-8') as f:
        for line in f:
            word = line.strip()

            if word:
                words.append(word)

    return words

TRANSLATION_FILE = "data/word_meanings.json"
translator = GoogleTranslator(source="en", target="ko")

def loadMeanings():
    try:
        with open(TRANSLATION_FILE,"r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def getMeaning(word, meanings):
    if word in meanings:
        return  meanings[word]

    try:
        meaning = translator.translate(word)
        meanings[word] = meaning

        with open(TRANSLATION_FILE,"w", encoding="utf-8") as f:
            json.dump(meanings, f, ensure_ascii=False, indent=2)

        return meaning
    except Exception:
        return "번역을 가져오지 못했습니다."


def playSound(file_path):
    mixer.music.load(file_path)
    mixer.music.play()


def gameRun(words, meanings):
    correct_count = 0
    start_time = time.time()

    for turn in range(1, 6):
        question = random.choice(words)

        print(f"\n[{turn}/5] 제시 단어: {question}")
        answer = input("입력: ").strip()

        if answer == question:
            print("정답")
            playSound("assets/good.wav")
            correct_count += 1
        else:
            print("오답")
            playSound("assets/bad.wav")

        print(f"뜻:{getMeaning(question, meanings)}")

    elapsed_time = time.time() - start_time
    return correct_count, elapsed_time


def scorePrint(score, elapsed_time):
    print("\n게임 종료")
    print(f"맞힌 개수: {score}")
    print(f"걸린 시간: {elapsed_time:}초")

    if score >= 3:
        print("합격")
    else:
        print("불합격")


def saveResult(elapsed_time, score):
    with open("word_game_score.csv","a",encoding="utf-8") as f:
        f.write(f"{elapsed_time:},{score}\n")

if __name__ == "__main__":
    words = wordLoad()
    meanings = loadMeanings()

    score, elapsed_time = gameRun(words, meanings)
    scorePrint(score, elapsed_time)
    saveResult(elapsed_time, score)
