# This shell script creates bilingual dictionaries from/to the given language from/to all languages
# that exist in the dict/ directory. Generated dictionaries go to the generated/ directory.
#
# Execute this script with one language code or name as the only parameter.
#     sh tools/generate_bilingual_dictionaries.sh <language>
#
# CC-BY 2024, Panlexia (https://github.com/barumau/panlexia)

# Check is the number of arguments equal to 0.
if [ $# -eq 0 ]
  then
    echo "The language code is missing."
    echo "Please run this script with a language code that has a corresponding .tsv file in dict/."
    echo "For example, create bilingual dictionaries from dict/E/eng.tsv (i.e. English) to other"
    echo "languages with the command below:"
    echo "    sh generate_bilingual_dictionaries.sh eng"
    return 1
fi

# Create generated directory if it doesn't exist yet.
mkdir -p generated

# The command below does the following things:
# - List the tree of files inside the dict directory.
#    dict/
#    ├── A
#    │   └── abk.tsv
#    └─── Z
#        └── zul.tsv
# - Filter in only the rows with the .tsv extension.
#    │   └── abk.tsv
#        └── zul.tsv
# - Delete characters before the filename.
#    abk.tsv
#    zul.tsv
# - Delete the .tsv suffix.
#    abk
#    zul
# - Write the dictionary names into a file called dict_list.txt.
tree dict/ | grep '\.tsv' | sed 's/.*─ //' | sed 's/\.tsv//' > dict_list.txt

# Generate bilingual dictionaries from the given language to all languages in dict_list.txt.
while read -r line; do python3 src/generate_bilingual_dict.py "$1" "$line"; done < dict_list.txt

# Generate bilingual dictionaries from all languages in dict_list.txt to the given language.
while read -r line; do python3 src/generate_bilingual_dict.py "$line" "$1"; done < dict_list.txt

# Build index by the name generated/index.md that includes links to the generated dictionaries.
python3 src/make_dict_index.py "$1" dict_list.txt

# Build website with MkDocs based on mkdocs.yml.
mkdocs build

# Delete the dict_list.txt file.
rm dict_list.txt