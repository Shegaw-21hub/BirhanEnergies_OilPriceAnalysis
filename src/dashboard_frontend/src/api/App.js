import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine } from 'recharts';
import './App.css'; // You can add custom styles here

const API_URL = 'http://127.0.0.1:5000';

function App() {
  const [priceData, setPriceData] = useState([]);
  const [eventData, setEventData] = useState([]);
  const [modelResults, setModelResults] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      fetch(`${API_URL}/api/data/prices`).then(res => res.json()),
      fetch(`${API_URL}/api/data/events`).then(res => res.json()),
      fetch(`${API_URL}/api/model/changepoint`).then(res => res.json())
    ]).then(([prices, events, model]) => {
      const formattedPrices = prices.map(item => ({
        ...item,
        Date: new Date(item.Date).getTime(),
      }));
      setPriceData(formattedPrices);
      setEventData(events);
      setModelResults(model);
      setLoading(false);
    }).catch(error => {
      console.error('Error fetching data:', error);
      setLoading(false);
    });
  }, []);

  if (loading) {
    return <div className="App">Loading dashboard...</div>;
  }
  
  const changepointDate = modelResults ? new Date(modelResults.most_probable_date).getTime() : null;

  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      const event = eventData.find(e => new Date(e.Date).getTime() === label);
      return (
        <div className="custom-tooltip" style={{ backgroundColor: 'white', padding: '10px', border: '1px solid #ccc' }}>
          <p>{`Date: ${new Date(label).toLocaleDateString()}`}</p>
          <p>{`Price: $${payload[0].value.toFixed(2)}`}</p>
          {event && <p>{`Event: ${event.Event}`}</p>}
        </div>
      );
    }
    return null;
  };

  return (
    <div className="App">
      <h1>Brent Oil Price Analysis Dashboard</h1>
      {modelResults && (
        <div style={{ padding: '10px', margin: '10px', border: '1px solid black' }}>
          <h2>Change Point Analysis Results</h2>
          <p>Most Probable Change Point: {modelResults.most_probable_date}</p>
          <p>Volatility before Change (sigma_1): {modelResults.sigma_1_mean.toFixed(4)}</p>
          <p>Volatility after Change (sigma_2): {modelResults.sigma_2_mean.toFixed(4)}</p>
        </div>
      )}
      <ResponsiveContainer width="95%" height={500}>
        <LineChart data={priceData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="Date" domain={['auto', 'auto']} tickFormatter={(unixTime) => new Date(unixTime).getFullYear()} type="number" scale="time"/>
          <YAxis />
          <Tooltip content={<CustomTooltip />} />
          <Legend />
          <Line type="monotone" dataKey="Price" stroke="#8884d8" dot={false} />
          {changepointDate && (<ReferenceLine x={changepointDate} stroke="red" strokeDasharray="5 5" label="Change Point" />)}
          {eventData.map((event, index) => (
            <ReferenceLine key={index} x={new Date(event.Date).getTime()} stroke="#82ca9d" strokeDasharray="5 5" label={{ value: event.Event, position: 'top', angle: -90, dx: -10 }} />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
export default App;