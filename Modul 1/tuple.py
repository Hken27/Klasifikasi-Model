def process_scores(scores_tuple):
    # a. Remove incomplete or empty entries
    scores_tuple = tuple(entry for entry in scores_tuple if entry and len(entry) == 2)

    # b. Remove entries with the same subject, keep only the highest score
    unique_scores = {}
    for subject, score in scores_tuple:
        if subject not in unique_scores or score > unique_scores[subject]:
            unique_scores[subject] = score

    scores_tuple = tuple((subject, score) for subject, score in unique_scores.items())

    # c. Calculate the total number of entries
    num_entries = len(scores_tuple)

    # d. Sort the entries by score from lowest to highest
    scores_tuple = tuple(sorted(scores_tuple, key=lambda x: x[1]))

    return scores_tuple, num_entries

scores = (
    ('Matematika', 85),
    ('Biologi', ),
    ('Kimia', 90),
    ('Fisika', 80),
    ('Matematika', 80),
    ('Biologi', 95),
    ('', 100),
    ('Fisika', 82)
)

processed_scores, num_entries = process_scores(scores)

print("Hasil pemrosesan:")
for entry, scores in processed_scores:
    print([entry, scores])
print("Total Entris Tersisa:", num_entries)