<?php

class BasketService
{
    public static function getAllBasket()
    {
        $url = API_BASE_URL . "/offers";
        $response = file_get_contents($url);
        return json_decode ($response, true);
    }

    public static function getAllFruits()
    {
        $url = API_BASE_URL . "/fruits";
        $response = file_get_contents($url);
        return json_decode ($response, true);
    }

    public static function getBasketContent(string $name_basket)
    {
        $url = API_BASE_URL . "/offers//" . rawurlencode($name_basket);
        $response = file_get_contents($url);
        return json_decode ($response, true);
    }
}