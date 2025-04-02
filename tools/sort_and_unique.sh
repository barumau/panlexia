# This shell script sorts and leaves only unique entries by deleting duplicates
# in monolingual dictionary files that exist in the dict/ directory.
#
# Execute this script with the following command.
#     sh tools/sort_and_unique.sh
#
# CC-BY 2025, Panlexia (https://github.com/barumau/panlexia)

sort_and_unique() {
    # The 1st parameter is the directory name.
    dir=$1
    echo $dir
    # Get language codes or names from the directory.
    tree $dir | grep '\.tsv' | sed 's/.*─ //' | sed 's/\.tsv//' > file_list.txt

    cat file_list.txt | while read line 
    do
        # Convert first character to uppercase.
        firstchar=`echo $line | cut -c1-1`
        firstchar=$(echo $firstchar | tr 'a-z' 'A-Z')
        # Filename form is 'dict/L/lang.tsv'
        filename="$dir/$firstchar/$line.tsv"
        # Keep row 1 unchanged, start from row 2, sort and leave only unique lines.
        (head -n 1 $filename && tail -n +2 $filename | LC_COLLATE=C sort | uniq) > temp.txt
        cp temp.txt $filename
    done

    # Delete temporary files.
    rm temp.txt
    rm file_list.txt
}

sort_and_unique dict
sort_and_unique concepts
