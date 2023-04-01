import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { CarShowAll } from './components/car/CarShowAll'
import React from 'react'

function App() {
  const [count, setCount] = useState(0)

  return (
    <React.Fragment>
      <CarShowAll/>
    </React.Fragment>
  )
}

export default App
