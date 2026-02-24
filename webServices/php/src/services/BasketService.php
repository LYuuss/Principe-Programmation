<?php

class BasketService
{
    public static function getAllBasket()
    {
        $url = API_BASE_URL , "/offers";
        $response = file_get_contents($url);
        return json_decode ($respone, true);
    }

    public static function getAllFruit()
    {
        $url = API_BASE_URL, "/fruits";
        $response = file_get_contents($url);
        return json_decode ($response, true);
    }
}