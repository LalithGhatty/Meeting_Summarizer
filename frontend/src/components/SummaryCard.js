import React from "react";

export default function SummaryCard({ title, content }) {
  return (
    <div className="bg-white shadow-md rounded-xl p-4 mb-4 border">
      <h2 className="text-xl font-semibold mb-2">{title}</h2>
      <pre className="whitespace-pre-wrap text-gray-700">{content}</pre>
    </div>
  );
}

