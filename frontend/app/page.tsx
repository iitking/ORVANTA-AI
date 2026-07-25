"use client";

import React from "react";
import Link from "next/link";
import {
  ArrowRight,
  BarChart3,
  Bot,
  Layers,
  ShieldCheck,
  Zap,
  TrendingUp,
  Cpu,
  Workflow
} from "lucide-react";

export default function HomePage() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col justify-between">
      {/* Hero Header */}
      <header className="px-8 py-6 flex items-center justify-between border-b border-slate-800/80">
        <div className="flex items-center gap-3">
          <div className="h-10 w-10 rounded-xl bg-gradient-to-tr from-blue-600 via-indigo-600 to-violet-500 flex items-center justify-center font-black text-white shadow-lg shadow-blue-500/20 text-lg">
            O
          </div>
          <div>
            <span className="font-extrabold text-xl tracking-tight text-white">ORVANTA AI</span>
            <span className="ml-2 text-xs px-2.5 py-0.5 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/20 font-medium">
              Autonomous B2B BI & Growth
            </span>
          </div>
        </div>

        <div className="flex items-center gap-4">
          <Link
            href="/dashboard"
            className="px-4 py-2 text-xs font-semibold rounded-xl bg-blue-600 hover:bg-blue-500 text-white shadow-md shadow-blue-500/20 transition flex items-center gap-1.5"
          >
            Launch Platform <ArrowRight className="w-3.5 h-3.5" />
          </Link>
        </div>
      </header>

      {/* Main Hero Section */}
      <main className="max-w-6xl w-full mx-auto px-6 py-16 text-center space-y-10">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-medium">
          <Zap className="w-3.5 h-3.5" /> Next-Gen Enterprise AI Operating System
        </div>

        <h1 className="text-4xl sm:text-6xl font-black tracking-tight text-white max-w-4xl mx-auto leading-tight">
          Turn business data into decisions, decisions into actions, and actions into{" "}
          <span className="bg-gradient-to-r from-blue-400 via-indigo-300 to-purple-400 bg-clip-text text-transparent">
            measurable growth.
          </span>
        </h1>

        <p className="text-base sm:text-lg text-slate-400 max-w-2xl mx-auto leading-relaxed">
          ORVANTA AI connects CRM systems, SQL databases, documents, and support tickets with autonomous LangGraph agents to observe, predict, and automate business operations.
        </p>

        {/* CTA Actions */}
        <div className="flex flex-wrap items-center justify-center gap-4 pt-4">
          <Link
            href="/dashboard"
            className="px-6 py-3.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-semibold text-sm shadow-xl shadow-blue-500/25 transition flex items-center gap-2"
          >
            <BarChart3 className="w-4 h-4" />
            Open Executive Dashboard
          </Link>
          <Link
            href="/ai-chat"
            className="px-6 py-3.5 rounded-xl bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-200 hover:text-white font-semibold text-sm transition flex items-center gap-2"
          >
            <Bot className="w-4 h-4 text-indigo-400" />
            Talk to AI Copilot
          </Link>
          <Link
            href="/integrations"
            className="px-6 py-3.5 rounded-xl bg-slate-900 border border-slate-800 hover:bg-slate-800 text-slate-200 hover:text-white font-semibold text-sm transition flex items-center gap-2"
          >
            <Workflow className="w-4 h-4 text-emerald-400" />
            Integration Hub
          </Link>
        </div>

        {/* Closed Loop Architecture Visual */}
        <div className="pt-12">
          <h2 className="text-xs uppercase tracking-widest text-slate-500 font-bold mb-6">
            The Closed-Loop Autonomous Loop
          </h2>
          <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3 text-xs font-semibold">
            {[
              "Observe",
              "Understand",
              "Analyze",
              "Predict",
              "Recommend",
              "Approve",
              "Execute",
              "Learn"
            ].map((step, idx) => (
              <div
                key={idx}
                className="p-3 rounded-xl bg-slate-900/80 border border-slate-800 flex flex-col items-center justify-center gap-1 hover:border-blue-500/40 transition"
              >
                <span className="text-[10px] text-blue-400 font-mono">0{idx + 1}</span>
                <span className="text-slate-200">{step}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Feature Highlights Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-10 text-left">
          <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-3">
            <div className="h-10 w-10 rounded-xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400">
              <Cpu className="w-5 h-5" />
            </div>
            <h3 className="font-bold text-white text-base">Multi-Agent LangGraph</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Specialized Data, Customer, Sales, Support, and Strategy agents collaborate asynchronously with complete auditability.
            </p>
          </div>

          <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-3">
            <div className="h-10 w-10 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400">
              <ShieldCheck className="w-5 h-5" />
            </div>
            <h3 className="font-bold text-white text-base">Human-In-The-Loop & Guardrails</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Zero reckless executions. High-risk actions require explicit human authorization with RBAC and prompt injection protection.
            </p>
          </div>

          <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-3">
            <div className="h-10 w-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
              <TrendingUp className="w-5 h-5" />
            </div>
            <h3 className="font-bold text-white text-base">Measurable Business ROI</h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Quantifies exactly how many hours were saved, how much ARR was protected from churn, and automated workflow completions.
            </p>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="px-8 py-6 border-t border-slate-900 text-center text-xs text-slate-500">
        ORVANTA AI &copy; 2026 &bull; All Rights Reserved &bull; <span className="text-slate-400 font-semibold">Nivesh Kumar Meena</span>
      </footer>
    </div>
  );
}
