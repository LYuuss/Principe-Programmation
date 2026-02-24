<h1>Liste des paniers</h1>

<ul>
<?php foreach ($names_baskets as $basket): ?>
    <li>
        <?= $basket["name"] ?>
    </li>
<?php endforeach; ?>
</ul> 
<br></br>