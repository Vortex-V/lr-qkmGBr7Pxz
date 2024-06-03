import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {models} from '../../models/models';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    60, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({alpha: true});

const controls = new OrbitControls(camera, renderer.domElement);
const loader = new GLTFLoader();


let App = function (config) {

    this.config = Object.assign({
        container: document.getElementById('app'),
        lights: {
            show: true,
            config: {
                forward: true,
                backward: true,
                right: true,
                left: true,
                bottom: true,
            }
        },
        plain: true,
        model: {
            show: true,
            name: 'floppa',
            type: 'gltf'
        },
        resolution: 1,
        rotating: false,
    }, config);

    const container = this.config.container;
    renderer.setSize(
        window.innerWidth * this.config.resolution,
        window.innerHeight * this.config.resolution, false);
    container.appendChild(renderer.domElement);

    function loadModel(model) {
        let source;
        switch (model.type) {
            case 'gltf':
                source = `${models[model.name]}/scene.gltf`;
                break;
            case 'gld':
                source = models[model.name];
                break;
            default:
                source = `${models[model.name]}/scene.gltf`
        }
        loader.load(`assets/models/${source}`, function (gltf) {
            scene.add(gltf.scene);
        }, undefined, function (error) {
            console.error(error);
        });
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

    function loadLights(lights) {
        const config = {
            forward: {x: 0, y: 10, z: 10}, // forward
            backward: {x: 0, y: 10, z: -10}, // backward
            right: {x: 10, y: 10, z: 0}, // right
            left: {x: -10, y: 10, z: 0}, // left
            bottom: {x: 0, y: -10, z: 0} // bottom
        };

        for (const [name, show] of Object.entries(lights.config)) {
            const position = config[name] || undefined;
            position !== undefined && show && scene.add(createLight(position));
        }
    }

    function runRotating() {
        controls.autoRotate = true;
        controls.autoRotateSpeed = 5;
    }

    this.run = function () {
        const config = this.config;
        config.plain && loadPlain();
        config.lights.show && loadLights(config.lights);
        config.model.show && loadModel(config.model);
        config.rotating && runRotating();

        camera.position.set(1, 1, 1);

        renderer.setAnimationLoop(() => {
            controls.update();
            renderer.render(scene, camera);
        });

    }

    function onWindowResize() {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();

        renderer.setSize(window.innerWidth, window.innerHeight)
    }

    window.addEventListener('resize', onWindowResize)
}

export default App;
