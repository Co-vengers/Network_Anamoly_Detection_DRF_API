import React, { useState } from "react";
import API from "../api/axios";

export default function Predict() {
  const [records, setRecords] = useState('[{"Feature1":12.3,"Feature2":0.5}]');
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    try {
      const res = await API.post("predict/run/", { records: JSON.parse(records) });
      setResult(res.data);
    } catch (err) {
      alert("Prediction failed: " + err.response?.data?.detail);
    }
  };

  return (
    <div>
      <h2>Predict</h2>
      <textarea
        rows={6}
        cols={50}
        value={records}
        onChange={(e) => setRecords(e.target.value)}
      />
      <br />
      <button onClick={handlePredict}>Predict</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
