#!/usr/bin/perl -w

my $serial = 0;
my $data1 = 0;
my $data2 = 0;

open (OUTPUTFILE1, "> ./scale_data.txt");
my $i =0;
my $totalrange = 300;
my $idlerange = 400;
for ($i =0; $i < $idlerange; $i++) {

    if ($i >= $totalrange/2) {
        if ($i % 5 eq 0) {
            $data2 = $data2 - 400;
            if ($data2 < 0 ) {
                $data2 = 0;
            }
        }
    }
    else {
        if ($i % 5 eq 0) {
            #$data1 = $data1 + 400;
            $data2 = $data2 + 400 + rand(2);
        }
    }
    if ($i >= $totalrange) {
        $data1 = 0; 
    }

    print OUTPUTFILE1 "$serial, $data2\n";
    #print OUTPUTFILE2 "$serial, $data1\n";
    #print "$serial,$data1\n";
    #print "$serial,$data2\n";
    $serial = $serial +1;
}
close(OUTPUTFILE1);
#close(OUTPUTFILE2);
