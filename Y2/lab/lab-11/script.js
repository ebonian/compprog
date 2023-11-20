async function generateChart() {
  // Write your code here. You can write your own function(s) if you want.
  if (window.chart) window.chart.destroy();

  const data = await fetch("https://restcountries.com/v3.1/all")
    .then((res) => {
      if (!res.ok) {
        console.error(res.status);
      }
      return res.json();
    })
    .catch((err) => {
      console.error(err);
    });

  if (!data) return;

  const numberOfCountries = parseInt(
    document.getElementById("numberOfCountries").value
  );

  if (isNaN(numberOfCountries)) return;

  const slicedData = data.slice(0, numberOfCountries);

  window.chart = new Chart(document.getElementById("barChart"), {
    type: "bar",
    data: {
      labels: slicedData.map((country) => country.name.common),
      datasets: [
        {
          label: "Total Population",
          data: slicedData.map((country) => country.population),
          backgroundColor: "rgb(221, 242, 242)",
          borderColor: "rgb(169, 222, 222)",
          borderWidth: 1.5,
        },
      ],
    },
  });
}
