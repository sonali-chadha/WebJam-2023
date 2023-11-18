import React from 'react';
import Navbar from '../src/components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from '../src/components/pages/Home';
import Services from '../src/components/pages/Services';
import SignUp from '../src/components/pages/SignUp';
import Map from './components/Map';
import ToDo from './components/pages/ToDo';



function App() {
  console.log("Made it to APP!");
  return (
    <>
    <Router>
      {/*<Navbar />*/}
      <Routes>
        <Route path='/' element={<Home />} exact />
        <Route path='/services' element={<Services/>} exact />
        <Route path='/map/:location' element={<ToDo animalName ='red_wolf'/>}  />
        <Route path='/sign-up' element={<SignUp/>} exact />
      </Routes>
    </Router>
     
    </>
  );
}

export default App;
