from os import name
import random

class EnglishGrammarHelper:
    def __init__(self):
        # Grammar contents covering past, present, and future tenses
        # Now includes multiple types of exercises: fill, underline, complete_lyrics
        self.grammar = {
            "present": {
                "simple present": {
                    "explanation": (
                        "Simple Present is used to describe habits, general truths, "
                        "and repeated actions.\n"
                        "Structure: Subject + base verb (add 's' or 'es' for third person singular).\n"
                        "Example: I eat. She eats."
                    ),
                    "examples": [
                        ("I (eat) breakfast every day.", "eat"),
                        ("She (go) to school by bus.", "goes"),
                        ("They (play) football on weekends.", "play"),
                    ],
                    "exercises": [
                        # fill-in-the-blank type
                        {"type": "fill", "sentence": "He (drink) water.", "answer": "drinks"},
                        {"type": "fill", "sentence": "We (study) English.", "answer": "study"},
                        {"type": "fill", "sentence": "Lisa (watch) TV every night.", "answer": "watches"},
                        {"type": "fill", "sentence": "My brother (work) in a bank.", "answer": "works"},
                        {"type": "fill", "sentence": "You (like) ice cream.", "answer": "like"},
                        {"type": "fill", "sentence": "She (do) her homework.", "answer": "does"},
                        {"type": "fill", "sentence": "The cats (sleep) on the sofa.", "answer": "sleep"},
                        # underline exercise type
                        {"type": "underline", "text": (
                            "Every day, he drinks water, studies English, "
                            "and watches TV before bed."
                        ), "correct_words": ["drinks", "studies", "watches"],
                         "instruction": "Underline the verbs in Simple Present tense."},
                        # complete lyrics exercise type
                        {"type": "complete_lyrics",
                         "lyrics": [
                             "She __(work) hard every day",
                             "We __(play) and laugh and say",
                             "You __(like) to sing this song"
                         ],
                         "answers": ["works", "play", "like"],
                         "instruction": "Complete the missing verbs in Simple Present."}
                    ],
                    "corrections": {
                        "drinks": "He is third person singular, so verb 'drink' changes to 'drinks'.",
                        "study": "We use base verb for 'we', so 'study' is correct.",
                        "watches": "'Lisa' is third person singular, so 'watch' → 'watches'.",
                        "works": "'My brother' is third person singular, so 'work' → 'works'.",
                        "like": "'You' uses base verb, so 'like' is correct here.",
                        "does": "'She' is third person singular, so 'do' changes to 'does'.",
                        "sleep": "'The cats' is plural, base verb is 'sleep'.",
                        # For underline type, explain the words
                        "drinks_underline": "'drinks' is a verb in Simple Present tense.",
                        "studies_underline": "'studies' is a verb in Simple Present tense.",
                        "watches_underline": "'watches' is a verb in Simple Present tense.",
                        # For lyrics answers
                        "works_lyrics": "Third person singular verb form for 'work'.",
                        "play_lyrics": "Base verb used with 'we'.",
                        "like_lyrics": "Base verb used with 'you'.",
                    }
                },
                "present continuous": {
                    "explanation": (
                        "Present Continuous is used to describe actions happening right now or temporary actions.\n"
                        "Structure: Subject + am/is/are + verb+ing.\n"
                        "Example: She is eating. They are playing."
                    ),
                    "examples": [
                        ("He (run) in the park now.", "is running"),
                        ("I (read) a book.", "am reading"),
                        ("They (watch) a movie.", "are watching"),
                    ],
                    "exercises": [
                        {"type": "fill", "sentence": "She (write) an email.", "answer": "is writing"},
                        {"type": "fill", "sentence": "We (play) chess.", "answer": "are playing"},
                        {"type": "fill", "sentence": "I (listen) to music.", "answer": "am listening"},
                        {"type": "fill", "sentence": "He (cook) dinner now.", "answer": "is cooking"},
                        {"type": "fill", "sentence": "They (dance) at the party.", "answer": "are dancing"},
                        {"type": "fill", "sentence": "You (study) for the exam.", "answer": "are studying"},
                        {"type": "fill", "sentence": "The dog (sleep) on the bed.", "answer": "is sleeping"},
                        {"type": "underline", "text": (
                            "Right now, she is writing a letter and they are dancing."
                        ), "correct_words": ["is writing", "are dancing"],
                         "instruction": "Underline the Present Continuous verbs in the text."},
                        {"type": "complete_lyrics",
                         "lyrics": [
                             "I am __(read) a book",
                             "They are __(play) outside",
                             "You are __(study) hard"
                         ],
                         "answers": ["reading", "playing", "studying"],
                         "instruction": "Complete the missing verbs in Present Continuous."}
                    ],
                    "corrections": {
                        "is writing": "She uses 'is' + verb+ing for Present Continuous.",
                        "are playing": "We use 'are' + verb+ing for Present Continuous.",
                        "am listening": "I use 'am' + verb+ing for Present Continuous.",
                        "is cooking": "'He' uses 'is' + verb+ing for Present Continuous.",
                        "are dancing": "'They' use 'are' + verb+ing for Present Continuous.",
                        "are studying": "'You' use 'are' + verb+ing for Present Continuous.",
                        "is sleeping": "'The dog' uses 'is' + verb+ing for Present Continuous.",
                        "is writing_underline": "'is writing' is Present Continuous verb structure.",
                        "are dancing_underline": "'are dancing' is Present Continuous verb structure.",
                        "reading_lyrics": "Present Continuous form of 'read'.",
                        "playing_lyrics": "Present Continuous form of 'play'.",
                        "studying_lyrics": "Present Continuous form of 'study'.",
                    }
                }
            },
            "past": {
                "simple past": {
                    "explanation": (
                        "Simple Past is used for completed actions in the past.\n"
                        "Structure: Subject + past verb.\n"
                        "Regular verbs add -ed; irregular verbs have special forms.\n"
                        "Example: I walked. She went."
                    ),
                    "examples": [
                        ("I (walk) to school yesterday.", "walked"),
                        ("She (go) to the market.", "went"),
                        ("They (play) football last week.", "played"),
                    ],
                    "exercises": [
                        {"type": "fill", "sentence": "He (visit) his friend.", "answer": "visited"},
                        {"type": "fill", "sentence": "We (see) a movie.", "answer": "saw"},
                        {"type": "fill", "sentence": "They (cook) dinner.", "answer": "cooked"},
                        {"type": "fill", "sentence": "I (buy) a new book.", "answer": "bought"},
                        {"type": "fill", "sentence": "She (study) all night.", "answer": "studied"},
                        {"type": "fill", "sentence": "You (drive) to work.", "answer": "drove"},
                        {"type": "fill", "sentence": "The children (play) in the park.", "answer": "played"},
                        {"type": "underline", "text": (
                            "Yesterday, he visited his friend, saw a movie, and cooked dinner."
                        ), "correct_words": ["visited", "saw", "cooked"],
                         "instruction": "Underline the verbs in Simple Past tense."},
                        {"type": "complete_lyrics",
                         "lyrics": [
                             "I __(walk) down the street",
                             "She __(go) to the store",
                             "They __(play) all day"
                         ],
                         "answers": ["walked", "went", "played"],
                         "instruction": "Complete the missing verbs in Simple Past."}
                    ],
                    "corrections": {
                        "visited": "Regular verb - add 'ed' to 'visit'.",
                        "saw": "'See' is irregular, past is 'saw'.",
                        "cooked": "Regular verb - add 'ed' to 'cook'.",
                        "bought": "'Buy' is irregular; past tense 'bought'.",
                        "studied": "Regular verb ending in consonant + 'y', changes 'y' to 'ied'.",
                        "drove": "'Drive' is irregular; past tense is 'drove'.",
                        "played": "Regular verb; add 'ed' to 'play'.",
                        "visited_underline": "'visited' is Simple Past verb.",
                        "saw_underline": "'saw' is Simple Past of 'see'.",
                        "cooked_underline": "'cooked' is Simple Past verb.",
                        "walked_lyrics": "Regular verb in Simple Past tense.",
                        "went_lyrics": "Irregular verb (go) past tense is 'went'.",
                        "played_lyrics": "Regular verb in Simple Past tense.",
                    }
                },
                "past continuous": {
                    "explanation": (
                        "Past Continuous describes an action that was ongoing in the past.\n"
                        "Structure: Subject + was/were + verb+ing.\n"
                        "Example: She was reading. They were dancing."
                    ),
                    "examples": [
                        ("I (watch) TV at 8pm.", "was watching"),
                        ("They (play) soccer.", "were playing"),
                        ("He (read) a book.", "was reading"),
                    ],
                    "exercises": [
                        {"type": "fill", "sentence": "She (write) a letter.", "answer": "was writing"},
                        {"type": "fill", "sentence": "We (listen) to music.", "answer": "were listening"},
                        {"type": "fill", "sentence": "I (cook) dinner.", "answer": "was cooking"},
                        {"type": "fill", "sentence": "They (dance) at 9pm.", "answer": "were dancing"},
                        {"type": "fill", "sentence": "He (drive) home.", "answer": "was driving"},
                        {"type": "fill", "sentence": "You (study) when I called.", "answer": "were studying"},
                        {"type": "fill", "sentence": "The baby (sleep) all night.", "answer": "was sleeping"},
                        {"type": "underline", "text": (
                            "She was writing a letter while they were dancing."
                        ), "correct_words": ["was writing", "were dancing"],
                         "instruction": "Underline the Past Continuous verbs in the text."},
                        {"type": "complete_lyrics",
                         "lyrics": [
                             "I was __(watch) TV",
                             "They were __(play) outside",
                             "You were __(study) hard"
                         ],
                         "answers": ["watching", "playing", "studying"],
                         "instruction": "Complete the missing verbs in Past Continuous."}
                    ],
                    "corrections": {
                        "was writing": "'She' uses 'was' + verb+ing for Past Continuous.",
                        "were listening": "'We' uses 'were' + verb+ing for Past Continuous.",
                        "was cooking": "'I' uses 'was' + verb+ing for Past Continuous.",
                        "were dancing": "'They' use 'were' + verb+ing for Past Continuous.",
                        "was driving": "'He' uses 'was' + verb+ing for Past Continuous.",
                        "were studying": "'You' use 'were' + verb+ing for Past Continuous.",
                        "was sleeping": "'The baby' uses 'was' + verb+ing for Past Continuous.",
                        "was writing_underline": "'was writing' is Past Continuous verb.",
                        "were dancing_underline": "'were dancing' is Past Continuous verb.",
                        "watching_lyrics": "Present participle verb form used with was/were.",
                        "playing_lyrics": "Present participle verb form used with was/were.",
                        "studying_lyrics": "Present participle verb form used with was/were.",
                    }
                }
            },
            "future": {
                "simple future": {
                    "explanation": (
                        "Simple Future indicates actions that will happen.\n"
                        "Structure: Subject + will + base verb.\n"
                        "Example: I will go. She will work."
                    ),
                    "examples": [
                        ("I (go) to the party tomorrow.", "will go"),
                        ("She (call) you later.", "will call"),
                        ("They (arrive) next week.", "will arrive"),
                    ],
                    "exercises": [
                        {"type": "fill", "sentence": "He (finish) his homework.", "answer": "will finish"},
                        {"type": "fill", "sentence": "We (travel) next month.", "answer": "will travel"},
                        {"type": "fill", "sentence": "I (help) you.", "answer": "will help"},
                        {"type": "fill", "sentence": "She (start) work soon.", "answer": "will start"},
                        {"type": "fill", "sentence": "They (visit) us tomorrow.", "answer": "will visit"},
                        {"type": "fill", "sentence": "You (send) the email.", "answer": "will send"},
                        {"type": "fill", "sentence": "It (rain) later.", "answer": "will rain"},
                        {"type": "underline", "text": (
                            "Tomorrow, he will finish his homework and she will start work."
                        ), "correct_words": ["will finish", "will start"],
                         "instruction": "Underline the verbs in Simple Future tense."},
                        {"type": "complete_lyrics",
                         "lyrics": [
                             "I will __(go) to school",
                             "They will __(travel) far",
                             "You will __(help) me"
                         ],
                         "answers": ["go", "travel", "help"],
                         "instruction": "Complete the missing verbs in Simple Future."}
                    ],
                    "corrections": {
                        "will finish": "'Will' + base verb denotes Simple Future.",
                        "will travel": "'Will' + base verb denotes Simple Future.",
                        "will help": "'Will' + base verb denotes Simple Future.",
                        "will start": "'Will' + base verb denotes Simple Future.",
                        "will visit": "'Will' + base verb denotes Simple Future.",
                        "will send": "'Will' + base verb denotes Simple Future.",
                        "will rain": "'Will' + base verb denotes Simple Future.",
                        "will finish_underline": "'will finish' is Simple Future verb.",
                        "will start_underline": "'will start' is Simple Future verb.",
                        "go_lyrics": "Base verb used with 'will' for future tense.",
                        "travel_lyrics": "Base verb used with 'will' for future tense.",
                        "help_lyrics": "Base verb used with 'will' for future tense.",
                    }
                },
                "future continuous": {
                    "explanation": (
                        "Future Continuous describes ongoing actions that will be happening in the future.\n"
                        "Structure: Subject + will be + verb+ing.\n"
                        "Example: She will be working. They will be playing."
                    ),
                    "examples": [
                        ("I (work) at 8pm tomorrow.", "will be working"),
                        ("They (play) soccer at that time.", "will be playing"),
                        ("He (study) all day.", "will be studying"),
                    ],
                    "exercises": [
                        {"type": "fill", "sentence": "She (write) a report at 5.", "answer": "will be writing"},
                        {"type": "fill", "sentence": "We (listen) to music then.", "answer": "will be listening"},
                        {"type": "fill", "sentence": "I (cook) dinner at 7.", "answer": "will be cooking"},
                        {"type": "fill", "sentence": "They (travel) at this time.", "answer": "will be traveling"},
                        {"type": "fill", "sentence": "He (drive) to work in the morning.", "answer": "will be driving"},
                        {"type": "fill", "sentence": "You (study) during the weekend.", "answer": "will be studying"},
                        {"type": "fill", "sentence": "She (read) a book.", "answer": "will be reading"},
                        {"type": "underline", "text": (
                            "At 9pm tomorrow, she will be writing and they will be traveling."
                        ), "correct_words": ["will be writing", "will be traveling"],
                         "instruction": "Underline the verbs in Future Continuous tense."},
                        {"type": "complete_lyrics",
                         "lyrics": [
                             "I will be __(work) late",
                             "They will be __(play) outside",
                             "You will be __(study) hard"
                         ],
                         "answers": ["working", "playing", "studying"],
                         "instruction": "Complete the missing verbs in Future Continuous."}
                    ],
                    "corrections": {
                        "will be writing": "'Will be' + verb+ing for Future Continuous.",
                        "will be listening": "'Will be' + verb+ing for Future Continuous.",
                        "will be cooking": "'Will be' + verb+ing for Future Continuous.",
                        "will be traveling": "'Will be' + verb+ing for Future Continuous.",
                        "will be driving": "'Will be' + verb+ing for Future Continuous.",
                        "will be studying": "'Will be' + verb+ing for Future Continuous.",
                        "will be reading": "'Will be' + verb+ing for Future Continuous.",
                        "will be writing_underline": "Future Continuous verb phrase.",
                        "will be traveling_underline": "Future Continuous verb phrase.",
                        "working_lyrics": "'working' is verb+ing form for Future Continuous.",
                        "playing_lyrics": "'playing' is verb+ing form for Future Continuous.",
                        "studying_lyrics": "'studying' is verb+ing form for Future Continuous.",
                    }
                }
            }
        }

    def list_grammar_topics(self):
        print("Available grammar topics:")
        for tense in self.grammar:
            print(f"  {tense.capitalize()}:")
            for topic in self.grammar[tense]:
                print(f"    - {topic.capitalize()}")

    def search_grammar(self, topic_name):
        topic_name = topic_name.lower()
        for tense, topics in self.grammar.items():
            for topic, content in topics.items():
                if topic == topic_name:
                    return tense, topic, content
        return None, None, None

    def generate_exercises(self, content, difficulty="easy"):
        # For now, difficulty filters number of exercises: easy=2, medium=4, hard=all
        exercises = content["exercises"]
        if difficulty == "easy":
            return exercises[:2]
        elif difficulty == "medium":
            return exercises[:4]
        else:
            return exercises

    def run_fill_exercise(self, exercise, corrections):
        print(f"\nFill in the blank:\n{exercise['sentence']}")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = exercise["answer"].lower()
        is_correct = (user_answer == correct_answer)
        if is_correct:
            print("Correct! ✔️")
        else:
            print(f"Incorrect. Correct answer: {correct_answer}")
        explanation = corrections.get(correct_answer, "No detailed explanation available.")
        print(f"Explanation: {explanation}")
        return is_correct

    def run_underline_exercise(self, exercise, corrections):
        print(f"\nUnderline Exercise:\n{exercise['instruction']}")
        print(f"Text: {exercise['text']}")
        print("Enter the words you think should be underlined, separated by commas:")
        user_input = input("Your answers: ").strip().lower()
        user_words = [w.strip() for w in user_input.split(",") if w.strip()]
        correct_words = [w.lower() for w in exercise["correct_words"]]

        correct_set = set(correct_words)
        user_set = set(user_words)

        correct_found = user_set.intersection(correct_set)
        missed = correct_set.difference(user_set)
        wrong = user_set.difference(correct_set)

        print("\nResults:")
        if correct_found:
            print(f"Correctly underlined: {', '.join(correct_found)}")
            for w in correct_found:
                k = f"{w}_underline"
                print(f"Explanation for '{w}': {corrections.get(k, 'No detailed explanation available.')}")
        else:
            print("No correct underlined words.")

        if missed:
            print(f"Missed words that should be underlined: {', '.join(missed)}")
        if wrong:
            print(f"Incorrectly underlined words: {', '.join(wrong)}")

        # Return True if user got all correct words and no wrong words
        is_correct = (len(missed) == 0 and len(wrong) == 0)
        if is_correct:
            print("Perfect! All correct words underlined.")
        else:
            print("Some mistakes found in underlining.")
        return is_correct

    def run_complete_lyrics_exercise(self, exercise, corrections):
        print(f"\nComplete the lyrics:\n{exercise['instruction']}")
        user_answers = []
        correct_answers = [a.lower() for a in exercise["answers"]]
        for i, line in enumerate(exercise["lyrics"], 1):
            print(f"{i}. {line}")
            ans = input("Your answer for the blank: ").strip().lower()
            user_answers.append(ans)

        correct_count = 0
        for i, user_ans in enumerate(user_answers):
            correct_answer = correct_answers[i]
            print(f"\nLine {i+1}:")
            print(f"Your answer: {user_ans}")
            print(f"Correct answer: {correct_answer}")
            explanation = corrections.get(f"{correct_answer}_lyrics", "No detailed explanation available.")
            if user_ans == correct_answer:
                print("Correct! ✔️")
                correct_count += 1
            else:
                print("Incorrect.")
            print(f"Explanation: {explanation}")

        print(f"\nYou got {correct_count} out of {len(correct_answers)} correct.")
        return correct_count == len(correct_answers)

    def run(self):
        print("Welcome to the English Grammar Helper!")
        print("You can search grammar topics (past, present, future tenses) and practice exercises.")
        print("Type 'list' to see all grammar topics.")
        print("Type 'exit' to quit.")
        while True:
            user_input = input("\nEnter a grammar topic to search or command: ").strip().lower()
            if user_input == "exit":
                print("Goodbye!")
                break
            elif user_input == "list":
                self.list_grammar_topics()
                continue
            elif user_input == "":
                continue

            tense, topic, content = self.search_grammar(user_input)
            if not content:
                print("Sorry, topic not found. Try again or type 'list' for available topics.")
                continue

            print(f"\n--- {topic.capitalize()} ({tense.capitalize()}) ---")
            print(content["explanation"])
            print("\nExamples:")
            for ex in content["examples"]:
                # sentence may have parentheses (verb), so replace if possible
                if len(ex) == 2:
                    sentence, answer = ex
                    displayed_sentence = sentence.replace(f"({answer})", answer)
                    print(f"  {displayed_sentence}")
                else:
                    print(f"  {ex}")

            difficulty = ""
            while difficulty not in ("easy", "medium", "hard"):
                difficulty = input("\nChoose exercise difficulty (easy/medium/hard): ").strip().lower()
                if difficulty not in ("easy", "medium", "hard"):
                    print("Please select from easy, medium, or hard.")

            exercises = self.generate_exercises(content, difficulty)

            print(f"\nExercises - {difficulty.capitalize()}:")
            for i, ex in enumerate(exercises, 1):
                ex_type = ex.get("type", "fill")
                print(f"\nExercise {i}:")
                if ex_type == "fill":
                    self.run_fill_exercise(ex, content["corrections"])
                elif ex_type == "underline":
                    self.run_underline_exercise(ex, content["corrections"])
                elif ex_type == "complete_lyrics":
                    self.run_complete_lyrics_exercise(ex, content["corrections"])
                else:
                    print("Unknown exercise type. Skipping...")

if __name__ == "__main__":
    app = EnglishGrammarHelper()
    app.run()
