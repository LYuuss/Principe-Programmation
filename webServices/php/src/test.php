<?php

$url = "http://127.0.0.1:5000/offers/universalBasket";
$response = file_get_contents($url);

echo "<pre>";
echo $response;
echo "</pres>\n";