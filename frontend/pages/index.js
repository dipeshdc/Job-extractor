import { useState } from "react";
import styles from "../styles/Home.module.css";

export default function Home() {
  const [url, setUrl] = useState("https://realpython.github.io/fake-jobs/");
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Backend API URL from environment or localhost
  const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

  const handleScrape = async () => {
    if (!url.trim()) {
      setError("Please enter a valid URL");
      return;
    }

    setLoading(true);
    setError("");
    setJobs([]);

    try {
      console.log(`Calling: ${BACKEND_URL}/api/scrape?url=${encodeURIComponent(url)}`);

      const response = await fetch(
        `${BACKEND_URL}/api/scrape?url=${encodeURIComponent(url)}`
      );

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || `Error: ${response.status}`);
      }

      const data = await response.json();

      if (data.status === "success") {
        setJobs(data.jobs);
        if (data.count === 0) {
          setError("No jobs found on this page. Try a different URL.");
        }
      } else {
        setError(data.message || "Failed to scrape jobs");
      }
    } catch (err) {
      console.error("Error:", err);
      setError(err.message || "An error occurred while scraping");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleScrape();
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1 className={styles.title}>💼 Job Extractor</h1>
        <p className={styles.subtitle}>
          Extract job listings from any website instantly
        </p>
      </div>

      <div className={styles.searchBox}>
        <input
          type="url"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="https://example.com/jobs"
          className={styles.input}
          disabled={loading}
        />
        <button
          onClick={handleScrape}
          disabled={loading}
          className={`${styles.button} ${loading ? styles.buttonLoading : ""}`}
        >
          {loading ? (
            <>
              <span className={styles.spinner}></span>
              Scraping...
            </>
          ) : (
            "Scrape Jobs"
          )}
        </button>
      </div>

      {error && <div className={styles.error}>{error}</div>}

      {jobs.length > 0 && (
        <div className={styles.stats}>
          🎉 Found <strong>{jobs.length}</strong> job
          {jobs.length === 1 ? "" : "s"}!
        </div>
      )}

      <div className={styles.jobsGrid}>
        {jobs.length === 0 && !loading && (
          <div className={styles.empty}>
            <p>👇 Enter a URL above and click "Scrape Jobs" to get started</p>
          </div>
        )}

        {jobs.map((job, idx) => (
          <div key={idx} className={styles.jobCard}>
            <div className={styles.jobHeader}>
              <h3 className={styles.jobTitle}>{job.title}</h3>
              <span className={styles.jobIndex}>#{idx + 1}</span>
            </div>

            <div className={styles.jobMeta}>
              <p className={styles.company}>
                <span className={styles.icon}>🏢</span> {job.company}
              </p>
              <p className={styles.location}>
                <span className={styles.icon}>📍</span> {job.location}
              </p>
            </div>

            <a
              href={job.url}
              target="_blank"
              rel="noopener noreferrer"
              className={styles.jobLink}
            >
              View Full Job →
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}
