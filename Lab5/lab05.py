import os
import string
import htmlFunctions as html


def load_stop_words(filepath):
    stopWords = set()
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            word = line.strip().lower()
            if word:
                stopWords.add(word)
    return stopWords


def clearPunctuation(mystring):
    for char in mystring:
        if char in string.punctuation:
            mystring = mystring.replace(char, '')
    return mystring


def get_speaker(line):
    stripped = line.strip()
    if not stripped.endswith(")"):
        return None
    lower = stripped.lower()
    if "trump" in lower:
        return "trump"
    elif "biden" in lower:
        return "biden"
    else:
        return "other"


def parseDebateFile(fd, stopWords, trumpDict, bidenDict):
    current_speaker = None
    for line in fd:
        line_stripped = line.strip()
        if not line_stripped:
            continue
        speaker = get_speaker(line_stripped)
        if speaker is not None:
            current_speaker = speaker
            continue
        if current_speaker not in ("trump", "biden"):
            continue
        target = trumpDict if current_speaker == "trump" else bidenDict
        for raw_word in line_stripped.split():
            clean_word = clearPunctuation(raw_word).lower()
            if not clean_word or clean_word in stopWords:
                continue
            target[clean_word] = target.get(clean_word, 0) + 1


def sort_descending(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


def print_dict(label, d, top_n=20):
    print(f"\n{'─' * 52}")
    print(f"  {label}  —  Top {top_n} words (descending)")
    print(f"{'─' * 52}")
    for i, (word, count) in enumerate(list(d.items())[:top_n], 1):
        print(f"  {i:>3}. {word:<28} {count}")


def generate_tag_cloud(speaker_name, wordDict, file_label, top_n=60):
    top_words  = list(wordDict.items())[:top_n]
    high_count = top_words[0][1]
    low_count  = top_words[-1][1]
    body = ""
    for word, cnt in top_words:
        body += " " + html.make_HTML_word(word, cnt, high_count, low_count)
    box      = html.make_HTML_box(body)
    filename = f"{speaker_name}_{file_label}"
    html.print_HTML_file(box, filename)
    print(f"  ✔  Tag cloud saved → {filename}.html")


if __name__ == "__main__":
    STOP_WORDS_FILE = "D:\\snake\\Uni\\Lab5\\stopWords.txt"
    DEBATE_FILES    = ["D:\\snake\\Uni\\Lab5\\debate_one.txt", "D:\\snake\\Uni\\Lab5\\debate_two.txt"]

    stopWords = load_stop_words(STOP_WORDS_FILE)
    debates = {}   

    for debate_file in DEBATE_FILES:
        file_label = os.path.basename(debate_file).replace(".txt", "").replace(" ", "_").title()
        trumpDict  = {}
        bidenDict  = {}
        with open(debate_file, encoding="utf-8") as fd:
            parseDebateFile(fd, stopWords, trumpDict, bidenDict)
        debates[file_label] = (sort_descending(trumpDict), sort_descending(bidenDict))

    for file_label, (trumpDict, bidenDict) in debates.items():
        print(f"\n{'═' * 52}")
        print(f"  {file_label.replace('_', ' ').upper()}")
        print(f"{'═' * 52}")
        print_dict(f"TRUMP — {file_label}", trumpDict, top_n=20)
        print_dict(f"BIDEN — {file_label}", bidenDict, top_n=20)
        print(f"\n  Trump unique words: {len(trumpDict)}")
        print(f"  Biden unique words: {len(bidenDict)}")

    print("\n")
    for file_label, (trumpDict, bidenDict) in debates.items():
        print(f"  Generating tag clouds for {file_label} …")
        generate_tag_cloud("Donald_Trump", trumpDict, file_label)
        generate_tag_cloud("Joe_Biden",    bidenDict, file_label)