import React, { useState } from 'react';
import './App.css';
import Person from './Person/Person';

const App = props => {
  const [ peopleState, setPeopleState ] = useState({
    people: [
      { name: 'Christian', age: 27 , job: 'Programmer'},
      { name: 'Nisma', age: 24 },
      { name: 'Leak', age: 26 },
    ],
    otherState: 'some other value',
  });

console.log(peopleState);

  const switchNameHandler = (newName) => {
    // console.log('Was clicked!');
    // this.state.people[0].name = 'Christiana'; DON'T DO THIS
    setPeopleState({
      people: [
        { name: newName, age: 27 },
        { name: 'Nisma', age: 24 },
        { name: 'Leak', age: 109 },
      ]
    });
  };



  return (
    <div className="App">
      <h1>Hi, I'm a React app</h1>
      <p>This is really working!!</p>
      <br/>
      <button className='Button' onClick={switchNameHandler.bind(this, 'Christian Haugen')}>Click this to switch some stuff around</button>
      <br/>
      <Person 
        name={peopleState.people[0].name} 
        age={peopleState.people[0].age} />
      <Person 
        name={peopleState.people[1].name} 
        age={peopleState.people[1].age} 
        click={switchNameHandler}>This is props.children (living in App.js but being passed through to the Person.js component)</Person>
      <br/>
      <Person 
        name={peopleState.people[2].name} 
        age={peopleState.people[2].age} />
      <br/>
    </div>
  );

}

export default App;