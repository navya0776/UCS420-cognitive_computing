import pandas as pd

roll_number = input("Enter your college roll number: ").strip()
last_digits = roll_number[-2:]
categories = ["billing", "account", "general"]

fixed_entries = [
    {"question": "what is the annual fee", "answer": "The annual fee is Rs 500.", "keywords": "fee cost price charge", "category": "billing"},
    {"question": "how to reset password", "answer": "Go to Settings > Reset Password.", "keywords": "password reset login", "category": "account"},
    {"question": "what are your working hours", "answer": "We are open 9 AM to 5 PM.", "keywords": "hours timing open time", "category": "general"},
    {"question": "how can i pay the fee", "answer": "You can pay via UPI, card, or net banking.", "keywords": "pay payment upi fee", "category": "billing"}
]

personal_entries = []

for digit in last_digits:
    category = categories[int(digit) % 3]
    if category == "billing":
        question = "how can i check my latest payment status"
        answer = "You can check your latest payment status in the billing section."
        keywords = "payment status billing"
    elif category == "account":
        question = "how do i update my registered mobile number"
        answer = "Open account settings and update your registered mobile number."
        keywords = "mobile number account"
    else:
        question = "where can i find the student help desk"
        answer = "The student help desk is available through the college support portal."
        keywords = "student help support"

    personal_entries.append({
        "question": question,
        "answer": answer,
        "keywords": keywords,
        "category": category
    })

df = pd.DataFrame(fixed_entries + personal_entries)
print("\nKnowledge base:")
print(df)

def score_query(query, data):
    query_words = set(query.lower().split())
    matches = []
    for index, entry in data.iterrows():
        searchable_text = f"{entry['question']} {entry['answer']} {entry['keywords']} {entry['category']}".lower()
        score = sum(word in searchable_text for word in query_words)
        if score > 0:
            matches.append((score, index, entry))
    matches.sort(key=lambda item: item[0], reverse=True)
    return matches

query = input("\nEnter a question to search the FAQ: ")
matches = score_query(query, df)
if matches:
    highest_score = matches[0][0]
    best_matches = [match for match in matches if match[0] == highest_score]
    print("\nTop matching FAQ entries:")
    for score, index, entry in best_matches:
        print(f"\nConfidence score: {score}")
        print(entry[["question", "answer", "keywords", "category"]].to_string())
    print("\nAll matches ranked by score:")
    for score, index, entry in matches:
        print(f"{score}: {entry['question']}")
else:
    print("No matching FAQ entries found.")

def same_category(category_name, data):
    return data[data["category"].str.lower() == category_name.lower()]

personal_category = personal_entries[0]["category"]
print(f"\nFAQ entries in the personalized category '{personal_category}':")
print(same_category(personal_category, df))

entry_index = int(input("\nChoose an FAQ row index from 0 to 5 to add a keyword: "))
if entry_index not in df.index:
    print("Invalid row index. No keyword was added.")
else:
    new_keyword = input("Enter a new keyword: ").strip()
    if new_keyword:
        existing_keywords = df.at[entry_index, "keywords"].split()
        if new_keyword.lower() not in [word.lower() for word in existing_keywords]:
            df.at[entry_index, "keywords"] = f"{df.at[entry_index, 'keywords']} {new_keyword}".strip()
        print("\nUpdated FAQ entry:")
        print(df.loc[entry_index])

df.to_csv(f"{roll_number}_faq_data.csv", index=False)
print(f"\nSaved the updated knowledge base to {roll_number}_faq_data.csv")

print("\nFAQ count per category:")
print(df.groupby("category").size())

print("\nTie demonstration:")
tie_matches = score_query("fee", df)
if tie_matches:
    highest_score = tie_matches[0][0]
    tied = [match for match in tie_matches if match[0] == highest_score]
    for score, index, entry in tied:
        print(f"Score: {score} | {entry['question']}")
else:
    print("No matches found.")

print("\nNon-tie demonstration:")
non_tie_matches = score_query("reset password", df)
if non_tie_matches:
    highest_score = non_tie_matches[0][0]
    best = [match for match in non_tie_matches if match[0] == highest_score]
    for score, index, entry in best:
        print(f"Score: {score} | {entry['question']}")
else:
    print("No matches found.")
