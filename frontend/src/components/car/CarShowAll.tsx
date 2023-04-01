import { useEffect, useState } from "react"
import { Car } from "../../models/Car"


export const CarShowAll = () => {
    const [cars, setCars] = useState([])
  
    useEffect(() => {
    fetch('http://127.0.0.1:8000/car/car/')
      .then(res => res.json())
      .then(data => setCars(data))
    }, []);
  
    return (
      <div className="App">
        <h1>Car list</h1>
        <table>
          <tr>
            <th>#</th>
            <th>Car brand</th>
            <th>Car make</th>
            <th>Car consumption</th>
            <th>Car color</th>
            <th>Car owner</th>
          </tr>
          {cars.map((car: Car, index) => (
            <tr key={index}>
              <td>{index}</td>
              <td>{car.brand}</td>
              <td>{car.make}</td>
              <td>{car.consumption}</td>
              <td>{car.color}</td>
              <td>{car.owner.name}</td>
            </tr>
          ))}
        </table>
  
      </div>
    )
  }