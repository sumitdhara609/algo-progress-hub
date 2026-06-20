import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Algo Progress Hub",
  description:
    "A progress dashboard for tracking algorithm practice, goals, streaks, and consistency.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}