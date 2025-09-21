<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Text to Speech (TTS)</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background-color: #eee;
            padding: 2px 6px;
            border-radius: 4px;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }
        .badge {
            display: inline-block;
            padding: 2px 8px;
            font-size: 0.8em;
            color: white;
            border-radius: 4px;
            margin-right: 5px;
        }
        .python { background-color: #3572A5; }
        .mit { background-color: #4CAF50; }
        .platform { background-color: #7f8c8d; }
        ul { margin-top: 0; }
    </style>
</head>
<body>

    <h1>🗣️ Text to Speech (TTS)</h1>

    <span class="badge python">Python 3.9+</span>
    <span class="badge mit">MIT License</span>
    <span class="badge platform">Windows | Linux | MacOS</span>

    <p>A Python project that converts text into <strong>natural-sounding speech</strong>. Supports multiple languages and can be integrated into Python applications or REST APIs.</p>

    <h2>🚀 Features</h2>
    <ul>
        <li>🔊 Convert text into clear and natural speech.</li>
        <li>🌍 Supports multiple languages and accents.</li>
        <li>💾 Save audio as MP3 or WAV files.</li>
        <li>🖥️ Easy-to-use CLI and Python module.</li>
        <li>⚡ Can be integrated with Flask API or other applications.</li>
        <li>🎛️ Adjustable voice, pitch, and speed (if engine supports).</li>
    </ul>

    <h2>🛠️ Installation</h2>
    <p>Clone the repository:</p>
    <pre><code>git clone https://github.com/youfa-lab/Text-to-Speech.git
cd Text-to-Speech
pip install -r requirements.txt</code></pre>

    <h2>📌 Usage</h2>

    <h3>1️⃣ Command Line (CLI)</h3>
    <pre><code>python main.py --text "Hello world" --lang en --output hello.mp3</code></pre>

    <h3>2️⃣ Python Module</h3>
    <pre><code>from tts import TextToSpeech

tts = TextToSpeech(lang="en")
tts.speak("Hello world")</code></pre>

    <h3>3️⃣ Flask API (Optional)</h3>
    <pre><code>python app.py</code></pre>
    <p>Send POST request:</p>
    <pre><code>POST http://localhost:5000/tts
Content-Type: application/json

{
  "text": "Hello world",
  "lang": "en"
}</code></pre>

    <h2>🧪 Roadmap</h2>
    <ul>
        <li>✅ CLI support</li>
        <li>✅ Python module</li>
        <li>✅ REST API support</li>
        <li>❌ Web-based UI</li>
        <li>❌ Voice customization (male/female)</li>
        <li>❌ Real-time streaming</li>
    </ul>

    <h2>📜 License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>. You are free to use, modify, and distribute it with proper attribution.</p>

</body>
</html>

