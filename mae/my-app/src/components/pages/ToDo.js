import React from "react";
import "../../App.css";
import { useParams } from "react-router-dom";
import  { Button } from '../Button';

const content = {
  eu: {
    title: "polar bear",
    video: '/Home page back.mp4',
    img: "https://i0.wp.com/wheelchairtravel.org/wp-content/uploads/2023/05/arc-de-triomphe-header.jpg?fit=2500%2C1333&ssl=1",
  },
  na: {
    title: "red wolf",
    video: '/Home page back.mp4',
    img: "https://tb-static.uber.com/prod/image-proc/processed_images/41e448619de9527990482249b90f154c/c9252e6c6cd289c588c3381bc77b1dfc.jpeg",
  },
};

export default function ToDo() {
  const params = useParams();
  return (
    <div className='to-do-container'>
      <video src = {content[params.location].video} autoPlay loop muted/>
      <h1> {content[params.location].title}</h1>

      <div className='to-do-list'>
        <div className="to-do-btns">
              <Button 
                link=""
                className='btns' 
                buttonStyle='btn--primary'
                buttonSize='btn--large'
                onClick={console.log('Todolist clicked')}>
                ADD TO DO<i/>
              </Button>
          </div>
      </div>
    </div>

  );
}
