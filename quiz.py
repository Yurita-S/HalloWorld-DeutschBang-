import random

def run_quiz(phrases):
    print("\n🧪 Quiz Mode - Choose the correct German translation!\n")
    score = 0
    total = min(3, len(phrases))

    for i in range(total):
        question = random.choice(phrases)
        correct = question['de']


        options = [correct]
        while len(options) < 4:
            candidate = random.choice(phrases)['de']
            if candidate not in options:
                options.append(candidate)
        random.shuffle(options)


        print(f"Q{i+1}: What is the German for '{question['en']}'?")
        for idx, opt in enumerate(options):
            print(f"  {idx + 1}. {opt}")


        answer = input("Your choice (1-4): ").strip()
        if answer.isdigit() and 1 <= int(answer) <= 4:
            if options[int(answer)-1] == correct:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was: {correct}\n")
        else:
            print("⚠️ Invalid input. Skipping question.\n")

    print(f"🏁 Quiz finished! Your score: {score}/{total}\n")
