def show_flashcards(phrases):
    print("\n📚 Flashcard Mode - Learn these fun phrases!\n")

    for i, phrase in enumerate(phrases, 1):
        input(f"{i}. EN: {phrase['en']} → Press Enter to show German")
        print(f"   DE: {phrase['de']}\n")

    print("🎉 You’ve reviewed all phrases in this category!\n")