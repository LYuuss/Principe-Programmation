<?php

$url = "http://127.0.0.1:5000/offers/universalBasket";
$response = file_get_contents($url);

//Décodage de JSON en tabelau PHP
$basket = json_decode($response, true);

echo "<pre>";
print_r($basket);
echo "</pres>\n";