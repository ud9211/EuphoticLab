const API_URL = 'http://127.0.0.1:5000';

export const getDishes = async () => {
  const response = await fetch(`${API_URL}/dishes`);
  const data = await response.json();
  return data;
};

export const togglePublishStatus = async (dishId) => {
  const response = await fetch(`${API_URL}/toggle_publish/${dishId}`, {
    method: 'POST'
  });
  const data = await response.json();
  return data;
};
