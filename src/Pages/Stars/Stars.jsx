import { useEffect, useState } from 'react';
import './Stars.css'
import axios from 'axios';

const Stars = ()=>{

    const [StarsData, setStarsData] = useState([]);

    const [CurrentObj, setCurrentObj] = useState({'Name': 'Earth'});

    useEffect(()=>{
        axios.get('http://localhost:5000/stars')
        .then((res)=>{
            setStarsData(res['data'])
            setCurrentObj(res['data'][0])
            // console.log(res)
        })
    }, [])

    const selectHandler = (e)=>{
        let selected = e.target.options[e.target.selectedIndex]
        // console.log(selected)
        let i = selected.getAttribute('data-key')
        // console.log(i)
        // console.log(e.target.options[e.target.selectedIndex])
        setCurrentObj(StarsData[i])
    }

    const attr_handler = (e)=>{
        
      }
    
    return (
        <div className="stars-ctn">
            <h1>Stars</h1>
            <select onChange={selectHandler} id='star-select'>
                {StarsData.map((p, i)=>{
                    return (
                        <option key={i} data-key={i}>{p['Name']}</option>
                    )
                })}
            </select>
            <div className="container">
            {Object.keys(CurrentObj).map((key) => (
                <p 
                    className='attr'
                    onClick={attr_handler}
                    key={key} 
                    data-key={key}
                    data-val={String(CurrentObj[key]).slice(0, 16)}
                >
                    {key}: {String(CurrentObj[key]).slice(0, 16)}
                </p>
                ))}
            </div>
                
        </div>
    )
}

export default Stars;
