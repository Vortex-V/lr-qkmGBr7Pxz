print "Password? ";
$a = <STDIN>;
chop $a;
until ($a eq "fred")
{
    print "sorry. Again? ";
    $a = <STDIN>;
    chop $a;
}
