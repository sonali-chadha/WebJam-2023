import WorldMap from "https://cdn.skypack.dev/react-world-map@2.3.0";
import React, {useState} from 'react';
import ReactDOM from 'react-dom';
import './Map.css';

function Map() {
  const [selected, onSelect] = React.useState('na');
  return (
    <div className='map-container'>
        <h1>Choose Your Region</h1>
        <WorldMap />
    </div>

  );
}

ReactDOM.render (
    <Map />,
    document.getElementById('root')
)

export default Map;
