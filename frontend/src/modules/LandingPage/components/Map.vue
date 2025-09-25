<script setup>
import { onMounted } from "vue";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

// Datos de las sucursales
const locations = [
    {
        coords: [23.181678522859173, -102.85988541019307],
        name: "Printek 🎨📎",
        color: "#3b82f6", // azul
        link: "https://maps.app.goo.gl/5hy2ytBUNfyfiacW7"
    },
    {
        coords: [23.18160154257846, -102.8600271745878],
        name: "Naranja Store 🛠🍊",
        color: "#f97316", // naranja
        link: "https://maps.app.goo.gl/NrToSVqo8CYWrWN49"
    },
    {
        coords: [23.181279053795965, -102.86241743797893],
        name: "Refaccionaria JOM 🚗🔧",
        color: "#3fc029", // verde}
        link: "https://maps.app.goo.gl/RYx2CTbtxbFBfu9Z9"
    },
];

onMounted(() => {
    const map = L.map("map").setView([23.18122, -102.86233], 18);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);

    locations.forEach(loc => {
        const icon = L.divIcon({
            className: "pulse-marker",
            html: `<div class="pulse-inner" style="background:${loc.color};"></div>`,
            iconSize: [30, 30],
        });

        const popupContent = `
          <div class="p-2 bg-white">
            <a href="${loc.link}" target="_blank" class="font-bold text-lg mb-1">${loc.name}</a>
          </div>
        `;

        L.marker(loc.coords, { icon }).addTo(map).bindPopup(popupContent).openPopup();
    });
});
</script>

<template>
    <div class="text-center mb-12">
        <h2 class="text-4xl md:text-5xl font-bold mb-6">
            Ven a
            <span class="text-transparent bg-gradient-to-r from-[#4ed636] to-[#048044] bg-clip-text">
                conocernos
            </span>
        </h2>

        <p class="text-xl text-muted-foreground max-w-3xl mx-auto">
            Visítanos en nuestras instalaciones o contáctanos para cualquier consulta. Estamos para servirte.
        </p>
    </div>
    <div id="map"
        class="z-1 w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl mx-auto my-12 lg:h-[600px] h-[400px] rounded-2xl shadow-lg">
    </div>
</template>
<style>
/* Contenedor transparente solo para el div interno */
.pulse-marker {
    width: 30px;
    height: 30px;
    position: relative;
}

/* Div interno con color y animación */
.pulse-inner {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    border: 3px solid #fff;
    box-shadow: 0 0 15px rgba(242, 242, 242, 0.3);
    position: relative;
}

.pulse-inner::after {
    content: "";
    position: absolute;
    left: 50%;
    top: 50%;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #69696962;
    transform: translate(-50%, -50%);
    animation: pulse 1.5s infinite;
}

/* Animación de pulso */
@keyframes pulse {
    0% {
        transform: translate(-50%, -50%) scale(1);
        opacity: 0.8;
    }

    100% {
        transform: translate(-50%, -50%) scale(2.5);
        opacity: 0;
    }
}

/* Popups más vistosos */
.leaflet-popup-content-wrapper {
    border-radius: 12px !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
}
</style>