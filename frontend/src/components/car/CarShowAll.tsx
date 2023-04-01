import { useEffect, useState } from "react"
import { Car } from "../../models/Car"


export const CarShowAll = () => {
    const [cars, setCars] = useState([])
  
    useEffect(() => {
    fetch('http://ec2-13-53-171-7.eu-north-1.compute.amazonaws.com/car/car/')
      .then(res => res.json())
      .then(data => setCars(data))
    }, []);
  
    return (
      <div className="App">
        <h1>Car list</h1>
        <table>
          <tr>
            <th>#</th>
            <th>Brand</th>
            <th>Make</th>
            <th>Consumption</th>
            <th>Color</th>
            <th>Owner</th>
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