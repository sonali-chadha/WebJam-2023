import React, { useEffect, useState} from "react";
import "../App.css";
import { Button } from "./Button";
import "./AnimalFacts.css";

function AnimalFact(props) {
    const [animalFacts, setFacts] = useState([])
    const [currentFact, setCurrent] = useState(0)
    const url = "https://8925-128-195-97-37.ngrok-free.app/" + props.animalName
    useEffect(() => {
    const fetchFact = async () => {
        const result = await fetch('https://corsproxy.io/?' + encodeURIComponent(url), {
            headers: {'ngrok-skip-browser-warning': 'yes'}
        });
        const factResults = await result.json();

        setFacts(factResults.message);
        setCurrent(0);
        console.log(factResults);
    }

    fetchFact()
    }, [])

    function changeFact () {
        //increment across animalFacts
        setCurrent((currentFact + 1)%animalFacts.length)
    }

    return (
        <>
            <p>{animalFacts[currentFact]}</p>
            <p>fact fact fact facjdlfkdssjklgajdslgjalk</p>

            <Button 
                link=""
                className='btn' 
                buttonStyle='btn--red'
                buttonSize='btn--large'
                onClick={changeFact}>
                Different Fact
            </Button>

        </>
        
    );
}

export {AnimalFact};


