import React from 'react';
import Navbar from '../src/components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from '../src/components/pages/Home';
import Services from '../src/components/pages/Services';
import Products from '../src/components/pages/Products';
import SignUp from '../src/components/pages/SignUp';



function App() {
  console.log("Made it to APP!");
  return (
    <>
    <Router>
      {/*<Navbar />*/}
      <Routes>
        <Route path='/' element={<Home />} exact />
        <Route path='/services' element={<Services/>} exact />
        <Route path='/products' element={<Products />} exact />
        <Route path='/sign-up' element={<SignUp/>} exact />
      </Routes>
    </Router>
     
    </>
  );
}

export default App;
