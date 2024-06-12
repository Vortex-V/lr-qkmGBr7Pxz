<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Домашняя страничка</title>
    <style>
        /* Стили тега body
        Установлен внешний отступ 0,
        отображение flex с позиционированием по центру,
        высота 100% от высоты экрана (100vh),
        шрифты без засечек.
        */
        body {
            margin: 0;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
            background-color: #474242;
            position: relative;

            font-family: sans-serif;
            font-size: 14px;
        }

        /* Стили фонового блока с шейдером
        Фискированная позиция позади всего контента на всю ширину и высоту экрана
        */
        .shader-background {
            position: fixed;
            width: 100vw;
            height: 100vh;
            z-index: -10;
        }

        .shader-background iframe {
            min-width: 100%;
            min-height: 100%;
        }

        /* Стили блока с контентом
        Отображение в режиме flex столбцом с центровкой содержимого блока,
        отображение поверх всего контента страницы,
        задний фон тёмный полупрозрачный, скругление углов блока
        */
        .content {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;

            z-index: 10;
            padding: 20px;

            background-color: rgba(23, 22, 22, 0.5);
            border-radius: 30px;
        }
    </style>
</head>
<body>
<div class="shader-background">
    <!-- Фрейм с шейдером -->
    <iframe width="640" height="360"
            src="https://www.shadertoy.com/embed/3tBGRm?gui=false&t=10&paused=false&muted=false" allowfullscreen></iframe>
</div>

<div class="content">
    <header>
        <h1>Здравствуйте, товарищи!</h1>
    </header>
    <main>
        <div id="about">
            <h2>О себе</h2>
            <p>
                <?= "Александров Виталий Евгеньевич.<br>" // Вывод текста ?>
                <span id="additional-bio"></span>
            </p>
            <?php
             // Получение версии PHP и вывод текста
            $phpversion = phpversion();
            echo "Страница работает на PHP $phpversion";
            ?>
        </div>

        <div id="video">
            <h2>Продукт отечественной рок музыки</h2>
            <h3>Radio Tapok - Петропавловск</h3>
             <!-- Фрейм с видеоплеером -->
            <?=
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/Lwf9ACmduHM?si=5dvrtcz-cTHis6od"
                    title="YouTube video player"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    allowfullscreen></iframe>'
            ?>
        </div>

        <div id="music">
            <h3>Radio Tapok - Ермак</h3>
            <!-- Аудиоплеер -->
            <?=
            '<audio controls>
                <source src="media/tapok_ermak.mp3" type="audio/mp3">
                Ваш браузер не поддерживает аудиоэлемент.
            </audio>'
            ?>
        </div>
    </main>
</div>

<script>
    let element = document.querySelector('#additional-bio');
    element.innerHTML = "Инженер-разработчик компании Клик2Майс";
</script>
</body>
</html>

