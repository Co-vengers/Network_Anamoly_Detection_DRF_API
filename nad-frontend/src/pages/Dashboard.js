import React from "react";
import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div>
      <h2>Dashboard</h2>
      <nav>
        <Link to="/upload">Upload Dataset</Link> |{" "}
        <Link to="/train">Train Model</Link> |{" "}
        <Link to="/predict">Predict</Link>
      </nav>
    </div>
  );
}
