<?php

$url = "http://127.0.0.1:5000/offers/universalBasket";
$response = file_get_contents($url);
$basket = json_decode($response, true);

echo "<h1>Liste des fruits dans le panier standard</h1>\n";

$number = 0;
foreach ($basket as $fruit) {
    $number = $number + 1;
    echo "Fruit ", $number, ": ", $fruit["name"] , " coming from ", $fruit["from"], " looking ", $fruit["color"], " <br>\n";
}