import { useNavigate } from 'react-router'
import './Navbar.css'

const Navbar = ()=>{

    const navigate = useNavigate();

    return (
        <div className='navbar-ctn'>
            <h2 id='title' onClick={()=>navigate('/')}>Cosmo</h2>
            <h2 onClick={()=>navigate('/planets')}>Planets</h2>
            <h2 onClick={()=>navigate('/stars')}>Stars</h2>
            <h2 onClick={()=>navigate('/query')}>Query</h2>

            {/* <div className="left">
                <h2>Cosmo</h2>
            </div>

            <div className="right">
                <h2>Explore</h2>
                <h2>Planets</h2>
                <h2>Stars</h2>
                <h2>Moons</h2>
            </div> */}

        </div>
    )
}

export default Navbar
