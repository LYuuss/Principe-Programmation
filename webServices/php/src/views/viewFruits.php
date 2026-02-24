<h1>Liste des fruits</h1>

<ul>
<?php foreach ($names_fruits as $fruit): ?>
    <li>
        <?= $fruit["name"] ?>
    </li>
<?php endforeach; ?>
</ul>
<br></br>