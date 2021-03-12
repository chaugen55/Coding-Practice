import React, { useState } from 'react';
import './App.css';
import Person from './Person/Person';

const App = props => {
  const [ peopleState, setPeopleState ] = useState({
    people: [
      { name: 'Christian', age: 27 },
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
      <button onClick={switchNameHandler.bind(this, 'still trying to understand this ish')}>Switch Name</button>
      <Person 
        name={peopleState.people[0].name} 
        age={peopleState.people[0].age} />
      <Person 
        name={peopleState.people[1].name} 
        age={peopleState.people[1].age} 
        click={switchNameHandler}/>
      <Person 
        name={peopleState.people[2].name} 
        age={peopleState.people[2].age} />
    </div>
  );

}

export default App;