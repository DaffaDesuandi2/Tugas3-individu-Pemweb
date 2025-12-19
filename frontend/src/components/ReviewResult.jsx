export default function ReviewResult({ result }) {
  if (!result) return null;

  return (
    <div className="card">
      <h3>Review Result</h3>
      <p><strong>Text:</strong> {result.review_text}</p>
      <p><strong>Sentiment:</strong> {result.sentiment}</p>
      <p><strong>Confidence:</strong> {result.confidence}</p>
      <p><strong>Key Points:</strong> {result.key_points}</p>
    </div>
  );
}
