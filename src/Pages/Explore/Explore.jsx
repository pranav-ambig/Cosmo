import './Explore.css'
import axios from 'axios'
import { useEffect, useState } from 'react'

const Explore = (props)=>{
  const [CurrentObj, setCurrentObj] = useState([{'name':''}])

  useEffect(()=>{
    axios.get('http://localhost:5000/init')
    .then((res)=>{
      setCurrentObj(res['data'][0])
    })
  }, [])

  const attr_handler = (e)=>{
    let rel = e.target.getAttribute('data-key')
    let relid = e.target.getAttribute('data-val')
    if (!rel.includes('ID')) return
    console.log(rel, relid)
    rel = rel.slice(0, rel.length-2)
    axios.post('http://localhost:5000/fetch', 
      {
        'rel': rel,
        'relid': relid
      }
    )
    .then((res)=>{
      setCurrentObj(res['data'][0])
    })
  }


  return (
    <>
      <h1>Explore</h1>

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
    </>
  )
}

export default Explore;
