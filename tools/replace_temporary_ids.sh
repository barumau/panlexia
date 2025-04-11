
replace_string_in_files() {
    echo "Replace $1 by $2 in $3/."
    # Finds string $1 in directory $3, and replaces it ($1) by string $2.
    grep -rl $1 $3 | xargs sed -i "s/$1/$2/g"
}

python3 src/check_new_concept_ids.py > old_to_new_ids.csv

cat old_to_new_ids.csv | while read line
do
    old_string="$(echo $line | cut -d',' -f1)"
    new_string="$(echo $line | cut -d',' -f2)"

    replace_string_in_files $old_string $new_string dict
    replace_string_in_files $old_string $new_string concepts
    replace_string_in_files $old_string $new_string data
done

rm old_to_new_ids.csv