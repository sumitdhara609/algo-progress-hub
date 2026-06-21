"use client";

import { useEffect, useMemo, useState } from "react";

import ProblemTable, { Problem } from "../components/ProblemTable";
import ProgressBar from "../components/ProgressBar";
import StatCard from "../components/StatCard";
import { supabase } from "../lib/supabase";

type CountMap = Record<string, number>;

type GoalSettings = {
  daily_goal: number;
  today_count: number;
  last_updated: string;
};

type StreakSettings = {
  current_streak: number;
  last_solved_date: string;
};

function countBy(problems: Problem[], key: keyof Problem): CountMap {
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
  const [problems, setProblems] = useState<Problem[]>([]);
  const [goal, setGoal] = useState<GoalSettings | null>(null);
  const [streak, setStreak] = useState<StreakSettings | null>(null);
  const [loading, setLoading] = useState(true);

  const [searchTerm, setSearchTerm] = useState("");
  const [difficultyFilter, setDifficultyFilter] = useState("All");
  const [statusFilter, setStatusFilter] = useState("All");

  async function loadDashboardData() {
    setLoading(true);

    const { data: problemsData, error: problemsError } = await supabase
      .from("problems")
      .select("*")
      .order("created_at", { ascending: false });

    const { data: goalData, error: goalError } = await supabase
      .from("goal_settings")
      .select("*")
      .eq("id", 1)
      .single();

    const { data: streakData, error: streakError } = await supabase
      .from("streak_settings")
      .select("*")
      .eq("id", 1)
      .single();

    if (problemsError) {
      console.error("Problems fetch error:", problemsError);
    }

    if (goalError) {
      console.error("Goal fetch error:", goalError);
    }

    if (streakError) {
      console.error("Streak fetch error:", streakError);
    }

    setProblems((problemsData ?? []) as Problem[]);
    setGoal(goalData as GoalSettings);
    setStreak(streakData as StreakSettings);

    setLoading(false);
  }

  useEffect(() => {
    loadDashboardData();
  }, []);

  const stats = useMemo(() => {
    const total = problems.length;

    const statusCount = countBy(problems, "status");
    const difficultyCount = countBy(problems, "difficulty");
    const topicCount = countBy(problems, "topic");
    const patternCount = countBy(problems, "pattern");

    const solved = statusCount["Solved"] || 0;
    const revision = statusCount["Revision"] || 0;
    const unsolved = statusCount["Unsolved"] || 0;

    const solvedPercentage = total > 0 ? (solved / total) * 100 : 0;

    return {
      total,
      solved,
      revision,
      unsolved,
      solvedPercentage,
      difficultyCount,
      topicCount,
      patternCount,
    };
  }, [problems]);

  const filteredProblems = useMemo(() => {
    return problems.filter((problem) => {
      const searchValue = searchTerm.trim().toLowerCase();

      const matchesSearch =
        searchValue.length === 0 ||
        problem.name.toLowerCase().includes(searchValue) ||
        problem.topic.toLowerCase().includes(searchValue) ||
        problem.pattern.toLowerCase().includes(searchValue) ||
        problem.status.toLowerCase().includes(searchValue) ||
        problem.difficulty.toLowerCase().includes(searchValue);

      const matchesDifficulty =
        difficultyFilter === "All" || problem.difficulty === difficultyFilter;

      const matchesStatus =
        statusFilter === "All" || problem.status === statusFilter;

      return matchesSearch && matchesDifficulty && matchesStatus;
    });
  }, [problems, searchTerm, difficultyFilter, statusFilter]);

  const dailyGoal = goal?.daily_goal || 0;
  const completedToday = goal?.today_count || 0;
  const dailyGoalProgress =
    dailyGoal > 0 ? Math.min((completedToday / dailyGoal) * 100, 100) : 0;

  const currentStreak = streak?.current_streak || 0;

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

      {loading ? (
        <section className="panel">
          <h2>Loading dashboard...</h2>
        </section>
      ) : (
        <>
          <section className="stats-grid">
            <StatCard
              label="Total Problems"
              value={stats.total}
              note="Tracked problems"
            />

            <StatCard
              label="Solved"
              value={stats.solved}
              note="Completed problems"
            />

            <StatCard
              label="Revision"
              value={stats.revision}
              note="Needs review"
            />

            <StatCard
              label="Unsolved"
              value={stats.unsolved}
              note="Pending practice"
            />
          </section>

          <section className="panel-grid">
            <div className="panel large-panel">
              <div className="section-heading">
                <p>Progress</p>
                <h2>Consistency Overview</h2>
              </div>

              <ProgressBar
                label="Solved Progress"
                value={stats.solvedPercentage}
              />

              <ProgressBar
                label="Daily Goal Progress"
                value={dailyGoalProgress}
              />

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
                {getTopEntries(stats.difficultyCount).map(([label, value]) => (
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
                {getTopEntries(stats.topicCount).map(([label, value]) => (
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
                {getTopEntries(stats.patternCount).map(([label, value]) => (
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

              <span>
                {filteredProblems.length} shown / {stats.total} total
              </span>
            </div>

            <div className="read-only-note">
              This public dashboard is read-only. Search and filters are enabled
              for exploration, while editing access is restricted.
            </div>

            <div className="filter-bar">
              <input
                value={searchTerm}
                onChange={(event) => setSearchTerm(event.target.value)}
                placeholder="Search by name, topic, pattern, status..."
              />

              <select
                value={difficultyFilter}
                onChange={(event) => setDifficultyFilter(event.target.value)}
              >
                <option>All</option>
                <option>Easy</option>
                <option>Medium</option>
                <option>Hard</option>
              </select>

              <select
                value={statusFilter}
                onChange={(event) => setStatusFilter(event.target.value)}
              >
                <option>All</option>
                <option>Solved</option>
                <option>Revision</option>
                <option>Unsolved</option>
              </select>
            </div>

            <ProblemTable problems={filteredProblems} />
          </section>
        </>
      )}

      <footer className="site-footer">
        <p>Built and maintained by</p>
        <strong>Sumit Dhara</strong>
      </footer>
    </main>
  );
}