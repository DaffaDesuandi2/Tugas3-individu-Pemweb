import { useEffect, useState } from "react";
import ReviewForm from "./components/ReviewForm";
import ReviewList from "./components/ReviewList";
import { getReviews } from "./api/reviewApi";

function App() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    getReviews().then(setReviews);
  }, []);

  function handleNewReview(review) {
    setReviews((prev) => [review, ...prev]);
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Product Review Analyzer</h1>
      <ReviewForm onNewReview={handleNewReview} />
      <ReviewList reviews={reviews} />
    </div>
  );
}

export default App;
