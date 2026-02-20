<?php

class BasketService
{
    public static function getAllBasket()
    {
        $url = API_BASE_URL , "/offers/universalBasket";
        $response = file_get_contents($url);
        return json_decode ($respone, true);
    }
}