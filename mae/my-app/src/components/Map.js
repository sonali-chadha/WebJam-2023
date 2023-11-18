import React, {useState} from 'react';
import WorldMap from 'react-world-map'
import ReactDOM from 'react-dom';
import './Map.css';
import  { Button } from './Button';

function Map() {
  const [selected, onSelect] = React.useState('na');
  console.log(selected)

  return (
    <div className='map-container'>
        <h1>Choose Your Region</h1>
        <WorldMap selected={selected} onSelect={onSelect}/>
        <div className="map-btns">
            <Button 
                link={"/map/" + selected}
                className='btns' 
                buttonStyle='btn--primary'
                buttonSize='btn--large'
                onClick={console.log('map loca choosen')}>
                SELECT REGION<i/>
            </Button>
        </div>
    </div>

  );
}

// ReactDOM.render (
//     <Map />,
//     document.getElementById('root')
// )

export default Map;
