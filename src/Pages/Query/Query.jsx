import { useEffect, useState } from 'react';
import './Query.css'
import axios from 'axios';

const Query = ()=>{

    const [Data, setData] = useState([]);
    
    const submitQuery = ()=>{
        let inp = document.getElementById('query-inp');
        axios.post('http://localhost:5000/query', {
            'query' : inp.value
        })
        .then((res)=>{
            if (res['data'] == 'Error') {
                console.log('error')
                let qt = document.getElementById('qbtn')
                qt.innerText = "Error!"
                setTimeout(()=>{qt.innerText = "Execute"}, 1000)
                setData([])
            }
            else {
                console.log(res['data'])
                setData(res['data'])
            }
        })
        
    }

    return (
        <div className="query-ctn">
            <h1>Query</h1>
            <textarea id='query-inp'></textarea>
            <button id='qbtn' onClick={submitQuery} style={{cursor: 'pointer'}}>Execute</button>

            {Data.map((r, i)=>{
                return (
                    <div key={i}>
                    {Object.keys(r).map((key) => (
                        <p key={key}>
                            {key}: {String(r[key]).slice(0, 16)}
                        </p>
                        ))}
                    </div>
                )
            })}
        </div>
    )
}

export default Query;
