import App from './app/App'
import WebGL from 'three/addons/capabilities/WebGL.js';

// Проверяет, что браузер поддерживает WebGL
if (WebGL.isWebGLAvailable()) {

    const appContainer = document.getElementById('app');

    // Получает имя модели из query параметра запроса
    const urlParams = new URLSearchParams(window.location.search);
    let model = urlParams.get('model');
    model = model === null ? 'kv2' : model;

    // Загружает приложение
    window.app = new App({
        container: appContainer,
        plain: false,
        lights: {
            show: true,
            config: {
                forward: 1,
                backward: 0,
                right: 1,
                left: 1,
                bottom: 0,
            }
        },
        model: {
            show: true,
            name: model,
        },
        resolution: 0.8,
        rotating: 0,
    });
    app.run();
} else {
    appContainer.appendChild(
        WebGL.getWebGLErrorMessage()
    );
}

