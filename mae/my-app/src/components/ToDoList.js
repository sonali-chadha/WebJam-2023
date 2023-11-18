import React from 'react';
import '../App.css';
import  { Button } from './Button';
import './ToDoList.css';

const TEMP = [
  {id: '1', complete: false, title: 'first'},
  {id: '2', complete: true, title: 'second'}
]

function ToDoList() {
  return (
    <div className='to-do-list-container'>
        <div className="ui container">
        <h1 className="ui center aligned header">To Do App</h1>

        <form className="ui form" action="/add" method="post">
            <div className="field">
                <label>Todo Title</label>
                <input type="text" name="title" placeholder="Enter Todo..."/>
            </div>
            <button className="ui blue button" type="submit">Add</button>
        </form>

        <hr/>
        {
          TEMP.map(todo => {
            return <div className="ui segment">
                <p className="ui big header">{todo.title || todo.id}</p>
            
                <span className={todo.complete ? "ui green label" : "ui gray label"}>
                  {todo.complete ? "Completed" : "Not Complete"}</span>
            
                <a className="ui blue button" href="/update/{{ todo.id }}">Update</a>
                <a className="ui red button" href="/delete/{{ todo.id }}">Delete</a>
            </div>
          })
        }

        </div>
    </div>
  );
}

export {ToDoList};
