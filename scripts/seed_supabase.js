const fs = require("fs");
const path = require("path");
const { createClient } = require("@supabase/supabase-js");

require("dotenv").config({ path: ".env.local" });

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  console.error("Missing Supabase environment variables.");
  process.exit(1);
}

const supabase = createClient(supabaseUrl, supabaseAnonKey);

async function seedProblems() {
  const filePath = path.join(__dirname, "..", "data", "problems.json");

  if (!fs.existsSync(filePath)) {
    console.error("data/problems.json not found.");
    process.exit(1);
  }

  const raw = fs.readFileSync(filePath, "utf-8");
  const problems = JSON.parse(raw);

  const rows = problems.map((problem) => ({
    name: problem.name,
    difficulty: problem.difficulty,
    topic: problem.topic,
    pattern: problem.pattern,
    status: problem.status,
    link: problem.link || "Custom",
    created_at: problem.created_at || new Date().toISOString(),
  }));

  const { data, error } = await supabase
    .from("problems")
    .insert(rows)
    .select();

  if (error) {
    console.error("Seed failed:");
    console.error(error);
    process.exit(1);
  }

  console.log(`Seed completed. Inserted ${data.length} problems.`);
}

seedProblems();