import App from './app/App'
import WebGL from 'three/addons/capabilities/WebGL.js';

if (WebGL.isWebGLAvailable()) {

    const appContainer = document.getElementById('app');

    const urlParams = new URLSearchParams(window.location.search);
    let model = urlParams.get('model');
    model = model === null ? 'kv2' : model;

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

