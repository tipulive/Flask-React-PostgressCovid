import React from 'react';

export default function TableDisplay({data}) {
  
    return (
    <>
   <div>
       <h1 className="text-primary text-center">Covid Data</h1>
   <table className="table table-striped table-dark">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Country</th>
      <th scope="col">Continent</th>
      <th scope="col">Confirmed</th>
      <th scope="col">Death</th>
      <th scope="col">Population</th>
    </tr>
  </thead>
  <tbody>
    {
data.map((item, i) => {
    return (
     
      <tr  key={i}>
     
      <td>{item[0]}</td>
      <td>{item[3]}</td>
      <td>{item[8]}</td>
      <td>{item[1]}</td>
      <td>{item[2]}</td>
      <td>{item[4]}</td>
    </tr>
    );
  })
    
    }
 </tbody>
</table>
   </div>
    </>
    )
}
