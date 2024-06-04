{
	s+=length($1)
}

END {
	print "Сумма: ", s
}
