import React from 'react';

const person = (props) => {
    return (
        <div className='Person'> 
            <p onClick={props.click}>Hi, I'm {props.name} and I am {props.age} years old!</p>
            <p>{props.children}</p>
        </div>
    )
};

export default person