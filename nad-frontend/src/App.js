import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Register from "./pages/Register";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import DatasetUpload from "./pages/DatasetUpload";
import TrainModel from "./pages/TrainModel";
import Predict from "./pages/Predict";
import PrivateRoute from "./components/PrivateRoute";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />

        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          }
        />
        <Route
          path="/upload"
          element={
            <PrivateRoute>
              <DatasetUpload />
            </PrivateRoute>
          }
        />
        <Route
          path="/train"
          element={
            <PrivateRoute>
              <TrainModel />
            </PrivateRoute>
          }
        />
        <Route
          path="/predict"
          element={
            <PrivateRoute>
              <Predict />
            </PrivateRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
