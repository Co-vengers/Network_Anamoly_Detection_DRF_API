import React, { useState } from "react";
import API from "../api/axios";

export default function TrainModel() {
  const [datasetId, setDatasetId] = useState("");
  const [params, setParams] = useState({ contamination: 0.01 });
  const [jobId, setJobId] = useState("");

  const startTraining = async () => {
    try {
      const res = await API.post("train/start/", {
        dataset_id: datasetId,
        params,
      });
      setJobId(res.data.job_id);
    } catch (err) {
      alert("Training failed: " + err.response?.data?.detail);
    }
  };

  return (
    <div>
      <h2>Train Model</h2>
      <input
        placeholder="Dataset UUID"
        value={datasetId}
        onChange={(e) => setDatasetId(e.target.value)}
      />
      <button onClick={startTraining}>Start Training</button>
      {jobId && <p>Training started. Job ID: {jobId}</p>}
    </div>
  );
}
