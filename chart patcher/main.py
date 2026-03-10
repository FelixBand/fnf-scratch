# Drop your FNF charts in the data.json file and run the script. It will format the chart so it works in my FNF Scratch rewrite.

import json

# Read the JSON file
with open('data.json') as file:
    data = json.load(file)

# Sort and remove duplicates for each "sectionNotes" array
for notes in data['song']['notes']:
    # Sort based on the first two values
    notes['sectionNotes'].sort(key=lambda x: (x[0], x[1]))

    # Remove duplicates based on the first two values, keeping the one with the higher third value
    unique_notes = []
    seen_combinations = {}
    for note in notes['sectionNotes']:
        key = (note[0], note[1])
        if key not in seen_combinations or note[2] > seen_combinations[key][2]:
            seen_combinations[key] = note

    # Update the "sectionNotes" array
    notes['sectionNotes'] = list(seen_combinations.values())

# Write the updated JSON back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=0)
exit()