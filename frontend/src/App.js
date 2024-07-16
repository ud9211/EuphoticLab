import React, { useEffect, useState } from 'react';
import { getDishes, togglePublishStatus } from './api';
import { subscribeToUpdates } from './ws';
import Dish from './Dish';

function App() {
  const [dishes, setDishes] = useState([]);

  useEffect(() => {
    fetchDishes();

    const handleUpdate = (updatedDish) => {
      setDishes((prevDishes) =>
        prevDishes.map((dish) =>
          dish.dishId === updatedDish.dishId ? updatedDish : dish
        )
      );
    };

    subscribeToUpdates(handleUpdate);
  }, []);

  const fetchDishes = async () => {
    const data = await getDishes();
    setDishes(data);
  };

  const handleTogglePublish = async (dishId) => {
    const updatedDish = await togglePublishStatus(dishId);
    setDishes((prevDishes) =>
      prevDishes.map((dish) =>
        dish.dishId === updatedDish.dishId ? updatedDish : dish
      )
    );
  };

  return (
    <div>
      <h1>Dish Dashboard</h1>
      <div>
        {dishes.map((dish) => (
          <Dish key={dish.dishId} dish={dish} onTogglePublish={handleTogglePublish} />
        ))}
      </div>
    </div>
  );
}

export default App;
