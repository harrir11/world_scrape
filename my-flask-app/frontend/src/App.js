import React, { useState } from 'react';

function App() {
  const [keyword, setKeyword] = useState('');
  const [graphUrl, setGraphUrl] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setGraphUrl('');

    const response = await fetch('http://localhost:5000/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ keyword })
    });

    if (response.ok) {
      setGraphUrl('http://localhost:5000/static/keyword_graph.png');
    } else {
      alert('No graph returned or error occurred.');
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>Reddit Keyword Scanner</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter keyword"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          required
          style={{ padding: '0.5rem', fontSize: '1rem' }}
        />
        <button type="submit" style={{ marginLeft: '1rem', padding: '0.5rem' }}>
          Generate Graph
        </button>
      </form>

      {graphUrl && (
        <div style={{ marginTop: '2rem' }}>
          <h2>Mentions Over Time</h2>
          <img src={graphUrl} alt="Reddit Keyword Chart" style={{ maxWidth: '100%' }} />
        </div>
      )}
    </div>
  );
}

export default App;
