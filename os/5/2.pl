open(FILE, '../4/nlist');
@list = <FILE>;
foreach $line (@list) {
    @column = split(' ', $line);
    if (@column[0] eq 'Бубнов') {
        print $line;
    }
}