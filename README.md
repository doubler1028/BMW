# BMW
import streamlit as st

# 스트림릿 컴포넌트로 HTML 및 JavaScript 삽입
html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D 룰렛 게임 - 벅샷 룰렛</title>
    <style>
        body { margin: 0; }
        canvas { display: block; }
    </style>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // 씬, 카메라, 렌더러 설정
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        var renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // 룰렛 휠을 만들기 위한 기초 설정
        var numSegments = 12; // 룰렛 칸의 수
        var radius = 5;
        var segments = [];
        var wheelSpeed = 0; // 휠 속도 (초기값)

        // 룰렛 휠의 각도 계산을 위한 함수
        function createRouletteWheel() {
            var geometry = new THREE.CylinderGeometry(radius, radius, 0.1, numSegments);
            var material = new THREE.MeshBasicMaterial({ color: 0xdddddd, wireframe: true });
            var wheel = new THREE.Mesh(geometry, material);
            wheel.rotation.x = Math.PI / 2;  // Y축을 기준으로 수평으로 배치
            scene.add(wheel);
            
            // 각 룰렛 칸을 색상으로 구분
            for (let i = 0; i < numSegments; i++) {
                var angle = (i / numSegments) * (2 * Math.PI);
                var color = new THREE.Color(Math.random(), Math.random(), Math.random()); // 랜덤 색상
                var segmentGeometry = new THREE.CylinderGeometry(radius, radius, 0.1, numSegments, 1, true, angle, Math.PI * 2 / numSegments);
                var segmentMaterial = new THREE.MeshBasicMaterial({ color: color, wireframe: false });
                var segment = new THREE.Mesh(segmentGeometry, segmentMaterial);
                scene.add(segment);
            }
        }

        // 애니메이션 루프
        function animate() {
            requestAnimationFrame(animate);
            
            // 룰렛 휠 회전
            if (wheelSpeed > 0) {
                scene.children[0].rotation.z += wheelSpeed;
                wheelSpeed *= 0.99; // 속도 감소
            }

            renderer.render(scene, camera);
        }

        // 카메라 설정
        camera.position.z = 10;

        // 룰렛 휠 생성
        createRouletteWheel();

        // 버튼 클릭으로 벅샷 룰렛 시작
        function startRoulette() {
            var randomSpeed = Math.random() * 0.2 + 0.5;  // 벅샷 효과를 위한 무작위 회전 속도
            wheelSpeed = randomSpeed;
        }

        // 벅샷 룰렛 버튼 이벤트
        window.addEventListener("click", function() {
            startRoulette();
        });

        animate();
    </script>
</body>
</html>
"""

# 스트림릿에서 HTML 렌더링
st.components.v1.html(html_string, height=600)
