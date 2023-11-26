import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import vid from './assets/earth2.mp4'

import Navbar from './components/NavBar'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Explore from './Pages/Explore/Explore'
import Planets from './Pages/Planets/Planets'
import Query from './Pages/Query/Query'
import Stars from './Pages/Stars/Stars'

function App() {

  return (
    <div className='app-ctn'>
      {/* <video autoPlay loop muted id='vid-ctn'>
        <source src={vid} type="video/mp4"/>
      </video> */}
      <BrowserRouter>
        <Navbar></Navbar>
        <Routes>
          <Route path='/' element={<Explore></Explore>}></Route>
          <Route path='/planets' element={<Planets></Planets>}></Route>
          <Route path='/query' element={<Query></Query>}></Route>
          <Route path='/stars' element={<Stars></Stars>}></Route>
        </Routes>
      </BrowserRouter>

    </div>
  )
}

export default App
