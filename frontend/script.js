const API_URL = "http://localhost:5000/weather";

const images = {
  "Córdoba": "https://4.bp.blogspot.com/-e9rBvKkXOIo/UP7g4GURFpI/AAAAAAAAAlc/60WkfFeDmX8/s1600/catedral_de_cordoba_argentina_night-1280x1024.jpg",
  "Buenos Aires": "https://www.getsready.com/wp-content/uploads/2016/10/the-city-center-of-Buenos-Aires.jpg",
  "Rio de Janeiro": "https://a.cdn-hotels.com/gdcs/production143/d357/42fb6908-dcd5-4edb-9f8c-76208494af80.jpg",
  "New York": "https://lovingnewyork.es/wp-content/uploads/2016/02/empire-state-mirador-161004120416001-1600x1067.jpeg",
  "Los Angeles": "https://static.independent.co.uk/2024/09/26/15/iStock-1463288473-1.jpg"
};

function loadWeather() {
  fetch(API_URL)
    .then(res => {
      if (!res.ok) {
        throw new Error("Error en la respuesta de la API");
      }
      return res.json();
    })
    .then(data => {
      const container = document.getElementById("weather-container");
      container.innerHTML = ""; 

      const latest = {};

      data.forEach(item => {
        if (!latest[item.ciudad]) {
          latest[item.ciudad] = item;
        }
      });

      Object.values(latest).forEach(item => {
        const card = document.createElement("div");
        card.className = "card";

        const img = images[item.ciudad] || "https://source.unsplash.com/300x200/?city";

        card.innerHTML = `
          <img src="${img}" alt="${item.ciudad}">
          <div class="card-content">
            <h2>${item.ciudad}</h2>
            <div class="temp">${item.temperatura}°C</div>
            <p>${item.clima}</p>
            <p>💧 ${item.humedad}%</p>
            <p>🌬️ ${item.viento} m/s</p>
          </div>
        `;

        container.appendChild(card);
      });
    })
    .catch(error => {
      console.error("Error al cargar datos:", error);

      const container = document.getElementById("weather-container");
      container.innerHTML = "<p>Error cargando datos 😢</p>";
    });
}

loadWeather();

setInterval(loadWeather, 60000);