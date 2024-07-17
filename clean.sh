input_file=$1
output_file=$2

sed '/^[0-9]/d' $input_file > $output_file
aspell check --dont-backup output_file

awk '
/CHAPTER/ {
    if (n > 0) {
        close(file)
    }
    n++
    file = "output/output_" n ".txt"
}
/CHAPTER/ || file != "" {
    print > file
}
' "$output_file"




