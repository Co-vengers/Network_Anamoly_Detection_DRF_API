import React, { useState } from "react";
import API from "../api/axios";

export default function DatasetUpload() {
  const [file, setFile] = useState(null);

  const handleUpload = async (e) => {
    e.preventDefault();
    const fd = new FormData();
    fd.append("csv_file", file);
    try {
      await API.post("datasets/", fd, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      alert("Dataset uploaded successfully!");
    } catch (err) {
      alert("Upload failed: " + err.response?.data?.detail);
    }
    console.log(fd.data)
  };

  return (
    <div>
      <h2>Upload Dataset</h2>
      <form onSubmit={handleUpload}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}
