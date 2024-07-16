import React from 'react';
import './Dish.css';

function Dish({ dish, onTogglePublish }) {
  return (
    <div className="dish-card">
      <h2 className="dish-title">{dish.dishName}</h2>
      <img src={dish.imageUrl} alt={dish.dishName} className="dish-image" />
      <p className="dish-status">Published: {dish.isPublished ? 'Yes' : 'No'}</p>
      <button className="toggle-button" onClick={() => onTogglePublish(dish.dishId)}>
        Toggle Publish
      </button>
    </div>
  );
}

export default Dish;
