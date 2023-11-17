import React from 'react';
import '../App.css';
import  { Button } from './Button';
import './HeroSection.css';


function HeroSection() {
  return (
    <div className='hero-container'>
        <video src='/Home page back.mp4' autoPlay loop muted />
        <h1>Endangered To-do</h1>
        

        <div className="hero-btns">
            <Button 
              link="/sign-up"
                className='btns' 
                buttonStyle='btn--primary'
                buttonSize='btn--large'
                onClick={console.log('animal creation')}>
                CHOSE YOUR ANIMAL<i className='far fa-play-circle'/>
            </Button>
        </div>
    </div>
  );
}

export default HeroSection;
