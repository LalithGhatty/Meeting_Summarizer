import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  // Use environment variable for API URL, fallback to localhost for development
  const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setError('');
      setResult(null);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select an audio file first');
      return;
    }

    setIsLoading(true);
    setError('');
    setResult(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      console.log('Uploading to:', API_BASE);
      const response = await fetch(`${API_BASE}/summarize`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Upload failed');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
      console.error('Upload error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            🎯 Meeting Summarizer
          </h1>
          <p className="text-lg text-gray-600">
            Upload your meeting audio to get an AI-powered summary
          </p>
        </div>

        {/* Upload Section */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <div className="border-2 border-dashed border-blue-300 rounded-lg p-8 text-center hover:bg-blue-50 transition-colors cursor-pointer">
            <input
              type="file"
              id="audioFile"
              accept="audio/*"
              onChange={handleFileChange}
              className="hidden"
            />
            <label htmlFor="audioFile" className="cursor-pointer">
              <div className="text-4xl mb-4">📁</div>
              <p className="text-lg font-medium text-gray-700 mb-2">
                {file ? `Selected: ${file.name}` : 'Click to select audio file'}
              </p>
              <p className="text-sm text-gray-500">
                Supports: MP3, WAV, M4A, and other audio formats
              </p>
            </label>
          </div>

          <div className="flex gap-4 mt-6">
            <button
              onClick={handleUpload}
              disabled={!file || isLoading}
              className="flex-1 bg-blue-600 text-white py-3 px-6 rounded-lg font-medium hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
            >
              {isLoading ? 'Processing...' : 'Summarize Meeting'}
            </button>
          </div>
        </div>

        {/* Loading State */}
        {isLoading && (
          <div className="bg-white rounded-lg shadow-md p-6 mb-6 text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
            <p className="text-gray-600">Processing your audio... This may take a minute.</p>
          </div>
        )}

        {/* Error State */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-6 mb-6">
            <div className="flex items-center mb-2">
              <span className="text-red-500 text-xl mr-2">⚠️</span>
              <h3 className="text-red-800 font-medium">Error</h3>
            </div>
            <p className="text-red-700">{error}</p>
          </div>
        )}

        {/* Results */}
        {result && (
          <div className="space-y-6">
            <div className={`p-4 rounded-lg ${result.mode === 'mock' ? 'bg-yellow-50 border border-yellow-200' : 'bg-green-50 border border-green-200'}`}>
              <p className={`font-medium ${result.mode === 'mock' ? 'text-yellow-800' : 'text-green-800'}`}>
                {result.mode === 'mock' ? '⚠️ Using mock data - Add OPENAI_API_KEY for real AI' : '✅ Using real AI processing'}
              </p>
            </div>

            {/* Summary Section */}
            <div className="bg-white rounded-lg shadow-md p-6">
              <h2 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
                📄 Meeting Summary
              </h2>
              <div className="bg-gray-50 rounded-lg p-4">
                <pre className="whitespace-pre-wrap text-gray-800 font-sans">
                  {result.summary}
                </pre>
              </div>
            </div>

            {/* Transcript Section */}
            <div className="bg-white rounded-lg shadow-md p-6">
              <h2 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
                🎧 Transcript
              </h2>
              <div className="bg-gray-50 rounded-lg p-4">
                <pre className="whitespace-pre-wrap text-gray-800 font-sans">
                  {result.transcript}
                </pre>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;