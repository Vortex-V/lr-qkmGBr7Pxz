import App from './app/App'
import WebGL from 'three/addons/capabilities/WebGL.js';

const appContainer = document.getElementById('app');

if (WebGL.isWebGLAvailable()) {
    window.app = new App({
        container: appContainer,
        model: false
    });
    app.run();
} else {
    appContainer.appendChild(
        WebGL.getWebGLErrorMessage()
    );
}

