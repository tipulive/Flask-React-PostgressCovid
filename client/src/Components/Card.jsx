import React from 'react';

export default function Card() {
  
    return (
    <>
   <div className="row row-cols-1 row-cols-sm-2 row-cols-md-4">
    <div className="col">
    <div className="card">
    
    <div className="card-body">
      <h4 className="card-title">John Doe</h4>
      <p className="card-text">Some example text some example text. John Doe is an architect and engineer</p>
      <a href="test.html" className="btn btn-primary">See Profile</a>
    </div>
  </div>

    </div>
    <div className="col">Column</div>
    <div className="col">Column</div>
    <div className="col">Column</div>
  </div>
    </>
    )
}
