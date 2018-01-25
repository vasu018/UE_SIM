#!/usr/bin/perl -w

my $serial = 0;
my $data1 = 0;
my $data2 = 0;

open (OUTPUTFILE1, "> ./scale_data.txt");
my $i =0;
my $totalrange = 300;
my $idlerange = 400;
my $step_size = 800;
my $seconds_bucket = 10; 
for ($i =0; $i < $idlerange; $i++) {
    if ($i < $seconds_bucket) {
        $data2 = 0;
        print OUTPUTFILE1 "$serial, $data2\n";
        #print OUTPUTFILE2 "$serial, $data1\n";
        #print "$serial,$data1\n";
        #print "$serial,$data2\n";
        $serial = $serial +1;
        
    }
    else {
        if ($i >= $totalrange/2) {
            if ($i % $seconds_bucket eq 0) {
                $data2 = $data2 - $step_size;
                if ($data2 < 0 ) {
                    $data2 = 0;
                }
            }
        }
        else {
            if ($i % $seconds_bucket eq 0) {
                #$data1 = $data1 + $step_size;
                $data2 = $data2 + $step_size + rand(2);
            }
        }
        if ($i > $totalrange) {
            $data2 = 0; 
        }

        print OUTPUTFILE1 "$serial, $data2\n";
        #print OUTPUTFILE2 "$serial, $data1\n";
        #print "$serial,$data1\n";
        #print "$serial,$data2\n";
        $serial = $serial +1;
    }
}
close(OUTPUTFILE1);
#close(OUTPUTFILE2);
