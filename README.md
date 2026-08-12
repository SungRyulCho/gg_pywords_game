# gg_pywords_game

영어 단어를 입력하는 콘솔 기반 워드 게임입니다.  
제시된 영어 단어를 5회 입력하고, 정답 수와 게임 시간을 확인할 수 있습니다.

## 주요 기능

- `data/word.txt` 파일에서 영어 단어 목록 불러오기
- 무작위 영어 단어 5개 제시
- 입력한 단어와 제시 단어 비교
- 정답 및 오답 소리 재생
- 게임 소요 시간과 정답 개수 출력
- 3개 이상 정답 시 합격, 2개 이하 정답 시 불합격
- 게임 결과를 CSV 파일에 누적 저장
- 단어의 한국어 뜻을 번역하여 화면에 출력
- 번역한 단어와 뜻을 `data/word_meanings.json`에 저장하여 재사용

## 프로젝트 구조

```text
gg_pywords_game/
├── assets/
│   ├── good.wav
│   └── bad.wav
├── data/
│   ├── word.txt
│   └── word_meanings.json
├── wordgame.py
├── word_game_score.csv
├── 알고리즘분석.md
├── pyproject.toml
└── README.md
```

## 실행 방법

```bash
uv sync
uv run python wordgame.py
```

## 사용 방법

1. 화면에 제시된 영어 단어를 확인합니다.
2. `입력:` 뒤에 같은 단어를 입력합니다.
3. 정답 또는 오답 결과와 단어의 한국어 뜻을 확인합니다.
4. 총 5회 반복 후 정답 개수, 걸린 시간, 합격 여부를 확인합니다.

## 합격 기준

| 맞힌 개수 | 결과 |
| --- | --- |
| 3개 이상 | 합격 |
| 2개 이하 | 불합격 |

## 사용 모듈

- `random`: 무작위 단어 선택
- `time`: 게임 시간 측정
- `pygame`: 정답 및 오답 소리 재생
- `deep-translator`: 영어 단어의 한국어 뜻 번역
- `json`: 번역 결과 저장 및 불러오기
