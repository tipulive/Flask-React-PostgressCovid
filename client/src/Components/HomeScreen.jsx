import React ,{useEffect,useState} from 'react';

import {DisplayCovidData} from '../Api';
import TableDisplay from './TableDisplay'


const HomeScreen=()=> {
    const [displayCovidTable,setisplayCovidTable]=useState([]);

    useEffect(() => {

        DisplayCovid();//on loading
     
    },[])

    async function DisplayCovid(){
       
        
        const CovidData=await DisplayCovidData();
        
        //console.log(CovidData.data);
        setisplayCovidTable(CovidData.data);
  
      }

      return (
        <>
     <div className="container">
     <TableDisplay data={displayCovidTable}/>
        
     </div>
    
        </>
      );
      
    
}

export default HomeScreen
