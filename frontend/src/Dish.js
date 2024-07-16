import React from 'react';

function Dish({ dish, onTogglePublish }) {
  return (
    <div style={{ border: '1px solid black', margin: '10px', padding: '10px' }}>
      <h2>{dish.dishName}</h2>
      <img src={dish.imageUrl} alt={dish.dishName} style={{ width: '200px' }} />
      <p>Published: {dish.isPublished ? 'Yes' : 'No'}</p>
      <button onClick={() => onTogglePublish(dish.dishId)}>
        Toggle Publish
      </button>
    </div>
  );
}

export default Dish;
