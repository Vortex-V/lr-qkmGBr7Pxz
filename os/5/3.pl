@arr = ('Здравствуй,', 'небо', 'в', 'облаках,');
print "@arr\n\n";
print "Последний элемент: $arr[$#arr]\n\n";

@arr2 = ('Здравствуй,', 'юность', 'в', 'сапогах!');
@mergedArr = (@arr, "\n", @arr2);

print "Слитно: ";
print @mergedArr;
print "\n\n";
print "Раздельно:\n @mergedArr\n\n";
print "Количество элементов: " . @mergedArr . "\n";
