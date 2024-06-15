print "Счётчик.\n";

$n;
sub counter {
	$n += 1;
	print "Count $n\n";
}

for ($i = 0; $i < 3; $i++) {
    &counter
}

print "\n\n";


print "Сумма переменных.\n";

sub sumFooBar {
	print "вызвана sumFooBar\n";
    $fred + $barney;
}
$foo = 3;
$bar = 4;
$c = &sumFooBar;
print "Результат (&sumFooBar): $c.\n";
$d = 3 * &sumFooBar;
print "Результат (3 * &sumFooBar): $d.\n";

print "\n\n";


print "Наибольшее значение.\n";

sub largerOfFooBar {
	if ($fred > $barney) {
        $fred;
    } else {
        $barney;
    }
}
$foo = 3;
$bar = 4;
$c = &largerOfFooBar;
print "Результат (&largerOfFooBar): $c.\n";

print "\n\n";


print "Интервал чисел.\n";

sub listOfFooBar {
	if ($foo < $bar) {		# Формирует интервал чисел от $fred до $barney (по возрастанию)
        $foo..$bar;
    } else {				# Формирует интервал чисел от $fred до $barney (по убыванию)
        reverse $bar..$foo;
    }
}
$foo = 11;
$bar = 6;
@c = &listOfFooBar; 	# Массив @c получает значения 11, 10, 9, 8, 7, 6
print "@c";

print "\n\n";


print "Работа с аргументами процедуры.\n";

sub max {
	if ($_[0] > $_[1]) {
        $_[0];
    } else	{
        $_[1];
    }
}
$c = &max(10, 15);      # Запишет 15 в переменную $c
$d = &max(5, 4, 10);    # Проигнорирует третий параметр и запишет 5 в переменную $c
print "Наибольшее из 10 и 15: $c\n";
print "Наибольшее из 5 и 4: $d\n";

print "\n\n";


print "Обработка аргументов в виде массива.\n";

$maximum = &max(3, 5, 10, 4, 6);
sub max {
    my $max = shift @_;
    foreach $el (@_) {
        if ($el > $max) {
            $max = $el;
        }
    }
    $max;
}
print "Максимальное из 3, 5, 10, 4, 6: $maximum";

print "\n\n";


print "Рекурсивный проход по каталогам.\n";

sub tree {
    my $dir = $_[0];
    opendir(ROOT, $dir);
    my @filelist = readdir(ROOT);
    closedir ROOT;
    foreach $x (@filelist) {
        if ($x ne "." and $x ne "..") {
            $y = "$dir/$x";
            if (-d $y) {
                print "\n$y:\n";
                tree($y);
            } else {
                print "$y\n";
            }
        }
    }
}
&tree("/tmp");

print "\n";
