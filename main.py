from phrases import PHRASES
from flashcard import show_flashcards
from quiz import run_quiz

def main():
    print("=" * 40)
    print("💬 HalloWorld (DeutschBang!) 💥")
    print("Learn quirky and romantic German phrases!")
    print("=" * 40)

    print("\n📚 Available categories:")
    for category in PHRASES:
        print(f" - {category}")

    category = input("\nChoose a category: ").strip().lower()
    if category not in PHRASES:
        print("❌ Invalid category. Exiting.")
        return

    print("\n🧪 Modes: flashcard / quiz")
    mode = input("Choose a mode: ").strip().lower()

    if mode == "flashcard":
        show_flashcards(PHRASES[category])
    elif mode == "quiz":
        run_quiz(PHRASES[category])
    else:
        print("❌ Invalid mode. Exiting.")

if __name__ == "__main__":
    main()
