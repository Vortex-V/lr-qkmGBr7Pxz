print "Введите число: ";
$num = <STDIN>;
chop $num;
$fac = 1;
$origNum = $num;
for ($i = 0; $i < $num; $i++) {
    $fac *= $num - $i;
}
print "Факториал $origNum = $fac \n";
