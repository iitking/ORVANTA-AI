import React from "react";
import "./globals.css";

export const metadata = {
  title: "ORVANTA AI — Autonomous B2B Business Intelligence & Growth Platform",
  description: "Turn business data into decisions, decisions into actions, and actions into measurable growth.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-slate-950 text-slate-100 antialiased min-h-screen">
        {children}
      </body>
    </html>
  );
}
