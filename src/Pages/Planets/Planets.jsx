import { useEffect, useState } from 'react';
import './Planets.css'
import axios from 'axios';

const Planets = ()=>{

    const [PlanetsData, setPlanetsData] = useState([]);

    const [CurrentObj, setCurrentObj] = useState({'Name': 'Earth'});

    useEffect(()=>{
        axios.get('http://localhost:5000/planets')
        .then((res)=>{
            setPlanetsData(res['data'])
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
        setCurrentObj(PlanetsData[i])
    }

    const attr_handler = (e)=>{
        // let rel = e.target.getAttribute('data-key')
        // let relid = e.target.getAttribute('data-val')
        // if (!rel.includes('ID')) return
        // console.log(rel, relid)
        // rel = rel.slice(0, rel.length-2)
        // axios.post('http://localhost:5000/fetch', 
        //   {
        //     'rel': rel,
        //     'relid': relid
        //   }
        // )
        // .then((res)=>{
        //   setCurrentObj(res['data'][0])
        // })
      }
    
    return (
        <div className="planets-ctn">
            <h1>Planets</h1>
            <select onChange={selectHandler} id='planet-select'>
                {PlanetsData.map((p, i)=>{
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

export default Planets;
