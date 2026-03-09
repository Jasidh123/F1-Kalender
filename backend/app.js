async function loadFlights(){

 const res = await fetch("http://127.0.0.1:5000/api/flights")
 const data = await res.json()

 const table = document.querySelector("#flights tbody")

 table.innerHTML = ""

 data.forEach(flight => {

  const row = `
  <tr>
   <td>${flight.aircraft}</td>
   <td>${flight.callsign}</td>
   <td>${flight.altitude}</td>
   <td>${flight.velocity}</td>
  </tr>
  `

  table.innerHTML += row

 })

}

loadFlights()

setInterval(loadFlights, 15000)
