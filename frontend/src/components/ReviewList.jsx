function ReviewList({ reviews }) {
  return (
    <div>
      <h2>Review Results</h2>

      {reviews.map((r) => (
        <div key={r.id} style={{ border: "1px solid #ccc", margin: "10px", padding: "10px" }}>
          <p><b>Review:</b> {r.review_text}</p>
          <p><b>Sentiment:</b> {r.sentiment ?? "Belum dianalisis"}</p>
          <p><b>Confidence:</b> {r.confidence ?? "-"}</p>
          <p><b>Key Points:</b> {r.key_points ?? "Tidak tersedia"}</p>
        </div>
      ))}
    </div>
  );
}

export default ReviewList;
