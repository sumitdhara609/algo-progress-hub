import { supabase } from "./supabase";

function getTodayDate() {
  return new Date().toISOString().split("T")[0];
}

function getDateDifferenceInDays(oldDate: string, newDate: string) {
  const oldTime = new Date(oldDate).setHours(0, 0, 0, 0);
  const newTime = new Date(newDate).setHours(0, 0, 0, 0);

  return Math.round((newTime - oldTime) / (1000 * 60 * 60 * 24));
}

export async function updateProgressAfterSolvedProblem() {
  const today = getTodayDate();

  const { data: goalData, error: goalFetchError } = await supabase
    .from("goal_settings")
    .select("*")
    .eq("id", 1)
    .single();

  if (goalFetchError) {
    console.error("Goal fetch error:", goalFetchError);
    return;
  }

  const goalLastUpdated = goalData.last_updated;
  const currentTodayCount =
    goalLastUpdated === today ? goalData.today_count : 0;

  const { error: goalUpdateError } = await supabase
    .from("goal_settings")
    .update({
      today_count: currentTodayCount + 1,
      last_updated: today,
    })
    .eq("id", 1);

  if (goalUpdateError) {
    console.error("Goal update error:", goalUpdateError);
  }

  const { data: streakData, error: streakFetchError } = await supabase
    .from("streak_settings")
    .select("*")
    .eq("id", 1)
    .single();

  if (streakFetchError) {
    console.error("Streak fetch error:", streakFetchError);
    return;
  }

  const lastSolvedDate = streakData.last_solved_date;

  if (lastSolvedDate === today) {
    return;
  }

  const dateDifference = getDateDifferenceInDays(lastSolvedDate, today);

  const nextStreak =
    dateDifference === 1 ? streakData.current_streak + 1 : 1;

  const { error: streakUpdateError } = await supabase
    .from("streak_settings")
    .update({
      current_streak: nextStreak,
      last_solved_date: today,
    })
    .eq("id", 1);

  if (streakUpdateError) {
    console.error("Streak update error:", streakUpdateError);
  }
}