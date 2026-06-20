import StatCard from "../components/StatCard";
import ProgressBar from "../components/ProgressBar";
import ProblemTable, { Problem } from "../components/ProblemTable";

import problemsData from "../data/problems.json";
import goalData from "../data/goal.json";
import streakData from "../data/streak.json";

type CountMap = Record<string, number>;

const problems = problemsData as Problem[];

function countBy(key: keyof Problem): CountMap {
  return problems.reduce((acc: CountMap, problem) => {
    const value = String(problem[key] ?? "Unknown");
    acc[value] = (acc[value] || 0) + 1;
    return acc;
  }, {});
}

function getTopEntries(map: CountMap, limit = 6) {
  return Object.entries(map)
    .sort((a, b) => b[1] - a[1])
    .slice(0, limit);
}

export default function Home() {
  const total = problems.length;

  const statusCount = countBy("status");
  const difficultyCount = countBy("difficulty");
  const topicCount = countBy("topic");
  const patternCount = countBy("pattern");

  const solved = statusCount["Solved"] || 0;
  const revision = statusCount["Revision"] || 0;
  const unsolved = statusCount["Unsolved"] || 0;

  const solvedPercentage = total > 0 ? (solved / total) * 100 : 0;

  const dailyGoal = goalData.daily_goal || 0;
  const completedToday = goalData.today_count || 0;
  const dailyGoalProgress =
    dailyGoal > 0 ? Math.min((completedToday / dailyGoal) * 100, 100) : 0;

  const currentStreak = streakData.current_streak || 0;

  return (
    <main className="page-shell">
      <section className="hero">
        <div className="hero-badge">Algorithm Practice Dashboard</div>

        <h1>Algo Progress Hub</h1>

        <p>
          A focused progress dashboard for tracking algorithm practice, problem
          status, streaks, goals, topics, and consistency.
        </p>
      </section>

      <section className="stats-grid">
        <StatCard label="Total Problems" value={total} note="Tracked problems" />
        <StatCard label="Solved" value={solved} note="Completed problems" />
        <StatCard label="Revision" value={revision} note="Needs review" />
        <StatCard label="Unsolved" value={unsolved} note="Pending practice" />
      </section>

      <section className="panel-grid">
        <div className="panel large-panel">
          <div className="section-heading">
            <p>Progress</p>
            <h2>Consistency Overview</h2>
          </div>

          <ProgressBar label="Solved Progress" value={solvedPercentage} />
          <ProgressBar label="Daily Goal Progress" value={dailyGoalProgress} />

          <div className="mini-stats">
            <div>
              <span>Current Streak</span>
              <strong>{currentStreak} day(s)</strong>
            </div>

            <div>
              <span>Daily Goal</span>
              <strong>{dailyGoal} problem(s)</strong>
            </div>

            <div>
              <span>Completed Today</span>
              <strong>{completedToday}</strong>
            </div>
          </div>
        </div>

        <div className="panel">
          <div className="section-heading">
            <p>Difficulty</p>
            <h2>Problem Level Split</h2>
          </div>

          <div className="breakdown-list">
            {getTopEntries(difficultyCount).map(([label, value]) => (
              <div className="breakdown-row" key={label}>
                <span>{label}</span>
                <strong>{value}</strong>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="panel-grid">
        <div className="panel">
          <div className="section-heading">
            <p>Topics</p>
            <h2>Most Practiced Areas</h2>
          </div>

          <div className="breakdown-list">
            {getTopEntries(topicCount).map(([label, value]) => (
              <div className="breakdown-row" key={label}>
                <span>{label}</span>
                <strong>{value}</strong>
              </div>
            ))}
          </div>
        </div>

        <div className="panel">
          <div className="section-heading">
            <p>Patterns</p>
            <h2>Recognized Problem Patterns</h2>
          </div>

          <div className="breakdown-list">
            {getTopEntries(patternCount).map(([label, value]) => (
              <div className="breakdown-row" key={label}>
                <span>{label}</span>
                <strong>{value}</strong>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="panel">
        <div className="section-heading table-heading">
          <div>
            <p>Problem Archive</p>
            <h2>Tracked Algorithm Problems</h2>
          </div>

          <span>{total} entries</span>
        </div>

        <ProblemTable problems={problems} />
      </section>
    </main>
  );
}