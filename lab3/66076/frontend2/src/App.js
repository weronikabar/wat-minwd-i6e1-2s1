import React from 'react';
import './App.css';
import MyDiagram from './components/MyDiagram';
import Buttons from './components/Buttons'


function App() {
    return (
        <div className="App">
            <header className="App-header">
                <Buttons/>
                <br></br>
                <MyDiagram />
            </header>
        </div>
    );
}

export default App;
