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

def playSound(file_path):
    mixer.music.load(file_path)
    mixer.music.play()


def gameRun(words):
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


words = wordLoad()
score, elapsed_time = gameRun(words)
scorePrint(score, elapsed_time)
saveResult(elapsed_time, score)
