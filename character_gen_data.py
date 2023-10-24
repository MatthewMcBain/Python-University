# Extracting the data from the JSON file and presenting it in a tabular format

import json

with open('/Users/Matt/OneDrive - Staffordshire University/University/Year 1/Software Development And Application '
          'Modelling/SDAM/week10/char_classes.json', 'r') as f:
    class_data = json.load(f)

print("{:<12} {:^10} {:^14} {:^8} {:^11} {:^12}".format("Class", "Strength", "Intelligence", "Wisdom", "Dexterity",
                                                        "Constitution"))
print("-" * 72)

for name, stats in class_data.items():
    print("{:<12} {:^10} {:^14} {:^8} {:^11} {:^12}".format(name.capitalize(),
                                                            stats['str'], stats['int'], stats['wis'], stats['dex'],
                                                            stats['con']))
