import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

const controls = new OrbitControls(camera, renderer.domElement);
const loader = new GLTFLoader();

const models = {
    floppa: 'floppa_but_bad',
    forestGod: 'princess_mononoke_-_forest_god',
    arny: 'the_head_of_the_sculpture_use_zbrush',
    tinker: 'the_thinker_by_auguste_rodin'
};

let App = function (config) {

    this.config = Object.assign({
        container: document.getElementById('app'),
        lights: true,
        plain: true,
        model: true,
        modelName: 'floppa',
    }, config);

    const container = config.container;
    renderer.setSize(window.innerWidth, window.innerHeight);
    container.appendChild(renderer.domElement);

    function loadModel(modelName) {
        loader.load(`assets/models/${models[modelName]}/scene.gltf`, function (gltf) {
            scene.add(gltf.scene);
        }, undefined, function (error) {
            console.error(error);
        });
    }

    function animate() {
        requestAnimationFrame(animate);

        controls.update();

        renderer.render(scene, camera);
    }

    function loadPlain() {
        const plain = new THREE.Mesh(
            new THREE.PlaneGeometry(1000, 1000),
            new THREE.MeshBasicMaterial({color: "#E2DFE1"})
        )
        plain.reciveShadow = true;
        plain.position.set(0, -1, 0)
        plain.rotateX(-Math.PI / 2);
        scene.add(plain)
    }

    function createLight(position, direction = {x: 0, y: 0, z: 0}) {
        const light = new THREE.DirectionalLight(0xffffff, 1);
        light.position.set(position.x, position.y, position.z);
        light.lookAt(direction.x, direction.y, direction.z);
        return light;
    }

    function loadLights() {
        scene
            .add(createLight({x: 0, y: 10, z: 10}))
            .add(createLight({x: 10, y: 10, z: 0}))
            .add(createLight({x: -10, y: 10, z: 0}))
            .add(createLight({x: 0, y: 10, z: -10}));
    }

    this.run = function () {
        if (this.config.plain) {
            loadPlain();
        }
        if (this.config.lights) {
            loadLights();
        }
        if (this.config.model) {
            loadModel(this.config.modelName);
        }

        camera.position.set(0, 5, 10);
        controls.update();

        renderer.setAnimationLoop(() => {
            animate();
        });

    }
}

export default App;
