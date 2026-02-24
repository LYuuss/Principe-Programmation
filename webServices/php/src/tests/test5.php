<?php

//post class BasketService
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../services/BasketService.php';

$names_baskets = BasketService::getAllBasket();

foreach($names_baskets as $basket) 
{
    echo $basket["name"] , "\n";
}