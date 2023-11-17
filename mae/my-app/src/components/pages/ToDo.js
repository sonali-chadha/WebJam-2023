import React from "react";
import "../../App.css";
import { useParams } from "react-router-dom";
import  { Button } from '../Button';

const content = {
  eu: {
    title: "polar bear",
    video: '/Polarbear-start.mp4',
    className: 'polar-bear',
  },
  na: {
    title: "red wolf",
    video: '/Redwolf-start.mp4',
    className: 'red-wolf',
  },
  as: {
    title: "snow leopard",
    video: '/Snowleo-start.mp4',
    className: 'snow-leo',
  },
  sa: {
    title: "The South America Page is Still Being Built!",
    video: '/Home page back.mp4',
    className: 'not-built',
  },
  af: {
    title: "The Africa Page is Still Being Built!",
    video: '/Home page back.mp4',
    className: 'not-built',
  },
  oc: {
    title: "The Oceania Page is Still Being Built!",
    video: '/Home page back.mp4',
    className: 'not-built',
  },
};

export default function ToDo() {
  const params = useParams();
  return (
    <div className='to-do-container'>
      <video src = {content[params.location].video} autoPlay loop muted/>
      <div className={content[params.location].className}>
      <h1> {content[params.location].title}</h1>

      <p>Insert a funfact here</p>

      <div className='to-do-list'>
        <div className="to-do-btns">
              <Button 
                link=""
                className='btn' 
                buttonStyle='btn--red'
                buttonSize='btn--large'
                onClick={console.log('Todolist clicked')}>
                ADD TO DO<i/>
              </Button>
          </div>
      </div>
      </div>
      
    </div>

  );
}
