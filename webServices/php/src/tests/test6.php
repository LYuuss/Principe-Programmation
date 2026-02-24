<?php

//post class BasketService
require_once __DIR__ . "/../config/config.php";
require_once __DIR__ . "/../services/BasketService.php";

$names_baskets = BasketService::getAllBasket();
$names_fruits = BasketService::getAllFruits();

$content_basket = BasketService::getBasketContent("universalBasket");

//Affichage
require_once __DIR__ . "/../views/viewBaskets.php";
require_once __DIR__ . "/../views/viewFruits.php";