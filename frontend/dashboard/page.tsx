"use client";

import React, { useState } from "react";
import { Navbar } from "../components/Navbar";
import {
  TrendingUp,
  TrendingDown,
  Users,
  DollarSign,
  AlertTriangle,
  Sparkles,
  CheckCircle2,
  XCircle,
  Clock,
  ArrowRight,
  ShieldCheck,
  Bot
} from "lucide-react";

export default function DashboardPage() {
  const [recommendations, setRecommendations] = useState([
    {
      id: "rec-1",
      title: "Initiate Executive Churn Intervention Campaign",
      desc: "Trigger automated customer success sequence and notify Account Executives in Slack.",
      roi: "$145K ARR protected",
      risk: "MEDIUM",
      status: "pending"
    },
    {
      id: "rec-2",
      title: "Roll Back Gateway v2.4 Patch",
      desc: "Revert to v2.3 to alleviate transaction errors for 2,341 customers.",
      roi: "Resolve 43% of payment support tickets immediately",
      risk: "HIGH",
      status: "pending"
    }
  ]);

  const handleDecision = (id: string, decision: "approved" | "dismissed") => {
    setRecommendations((prev) =>
      prev.map((r) => (r.id === id ? { ...r, status: decision } : r))
    );
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      <Navbar />

      <main className="flex-1 max-w-7xl w-full mx-auto px-6 py-8 space-y-8">
        {/* Welcome Header */}
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-6">
          <div>
            <h1 className="text-3xl font-extrabold tracking-tight text-white flex items-center gap-3">
              Executive Business Intelligence
              <span className="text-xs px-2.5 py-1 rounded-md bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-medium">
                Live Data Connected
              </span>
            </h1>
            <p className="text-sm text-slate-400 mt-1">
              Autonomous observation loop active across CRM, Database, Support, and Financial streams.
            </p>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-xs text-slate-400">Next Autonomous Run:</span>
            <span className="text-xs font-mono bg-slate-900 border border-slate-800 px-2.5 py-1 rounded text-slate-300">
              in 04:18
            </span>
          </div>
        </div>

        {/* Top KPI Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          <div className="p-5 rounded-2xl bg-slate-900/70 border border-slate-800 hover:border-slate-700 transition">
            <div className="flex items-center justify-between text-slate-400 text-sm font-medium">
              <span>Monthly Recurring ARR</span>
              <DollarSign className="w-4 h-4 text-emerald-400" />
            </div>
            <div className="mt-3 flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-white">$2.4M</span>
              <span className="text-xs font-semibold text-emerald-400 flex items-center">
                <TrendingUp className="w-3.5 h-3.5 mr-0.5" /> +12.4%
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-1">vs. previous 30 days</p>
          </div>

          <div className="p-5 rounded-2xl bg-slate-900/70 border border-slate-800 hover:border-slate-700 transition">
            <div className="flex items-center justify-between text-slate-400 text-sm font-medium">
              <span>Active Customers</span>
              <Users className="w-4 h-4 text-blue-400" />
            </div>
            <div className="mt-3 flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-white">18,420</span>
              <span className="text-xs font-semibold text-emerald-400 flex items-center">
                <TrendingUp className="w-3.5 h-3.5 mr-0.5" /> +8.1%
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-1">Net additions: +1,380</p>
          </div>

          <div className="p-5 rounded-2xl bg-slate-900/70 border border-slate-800 hover:border-slate-700 transition">
            <div className="flex items-center justify-between text-slate-400 text-sm font-medium">
              <span>Customer Churn Rate</span>
              <TrendingDown className="w-4 h-4 text-amber-400" />
            </div>
            <div className="mt-3 flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-white">4.2%</span>
              <span className="text-xs font-semibold text-emerald-400 flex items-center">
                <TrendingDown className="w-3.5 h-3.5 mr-0.5" /> -1.3%
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-1">Target benchmark: &lt; 5.0%</p>
          </div>

          <div className="p-5 rounded-2xl bg-slate-900/70 border border-slate-800 hover:border-slate-700 transition">
            <div className="flex items-center justify-between text-slate-400 text-sm font-medium">
              <span>Revenue Protected by AI</span>
              <ShieldCheck className="w-4 h-4 text-indigo-400" />
            </div>
            <div className="mt-3 flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-white">$384K</span>
              <span className="text-xs font-semibold text-indigo-400 flex items-center">
                +24 actions
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-1">via autonomous interventions</p>
          </div>
        </div>

        {/* Middle Section: AI Insights & AI Recommendations */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* AI Insights Feed */}
          <div className="p-6 rounded-2xl bg-slate-900/80 border border-slate-800 space-y-5">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Sparkles className="w-5 h-5 text-indigo-400" />
                <h2 className="text-lg font-bold text-white">AI Business Insights</h2>
              </div>
              <span className="text-xs text-slate-400">Continuously Observed</span>
            </div>

            <div className="space-y-3.5">
              <div className="p-4 rounded-xl bg-red-950/20 border border-red-900/40 hover:border-red-800/60 transition">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-red-400 uppercase tracking-wider flex items-center gap-1.5">
                    <span className="h-2 w-2 rounded-full bg-red-500"></span> Churn Alert
                  </span>
                  <span className="text-xs font-bold text-red-300">$184K ARR at risk</span>
                </div>
                <h3 className="font-semibold text-white mt-1.5">23 Enterprise accounts at high churn risk</h3>
                <p className="text-xs text-slate-400 mt-1">
                  Product usage down 24%, support tickets up 41%. Highest risk customer: ABC Corp (78% probability).
                </p>
              </div>

              <div className="p-4 rounded-xl bg-emerald-950/20 border border-emerald-900/40 hover:border-emerald-800/60 transition">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
                    <span className="h-2 w-2 rounded-full bg-emerald-500"></span> Growth Opportunity
                  </span>
                  <span className="text-xs font-bold text-emerald-300">+$210K potential ARR</span>
                </div>
                <h3 className="font-semibold text-white mt-1.5">Expansion Opportunity in Enterprise Tier</h3>
                <p className="text-xs text-slate-400 mt-1">
                  Advanced Analytics module feature retention is 94% with low price sensitivity. Recommending +8% tier adjustment.
                </p>
              </div>

              <div className="p-4 rounded-xl bg-amber-950/20 border border-amber-900/40 hover:border-amber-800/60 transition">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
                    <span className="h-2 w-2 rounded-full bg-amber-500"></span> Root-Cause Anomaly
                  </span>
                  <span className="text-xs font-bold text-amber-300">2,341 affected</span>
                </div>
                <h3 className="font-semibold text-white mt-1.5">Support tickets increased 32% (Payment Failures)</h3>
                <p className="text-xs text-slate-400 mt-1">
                  Correlated to Payment Gateway v2.4 patch rollout. Estimated $47K revenue settlement delay.
                </p>
              </div>

              <div className="p-4 rounded-xl bg-blue-950/20 border border-blue-900/40 hover:border-blue-800/60 transition">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
                    <span className="h-2 w-2 rounded-full bg-blue-500"></span> Sales Velocity
                  </span>
                  <span className="text-xs font-bold text-blue-300">+$320K pipeline</span>
                </div>
                <h3 className="font-semibold text-white mt-1.5">Enterprise conversion increased 18%</h3>
                <p className="text-xs text-slate-400 mt-1">
                  Google (Score: 92) and Microsoft (Score: 89) flagged as hot high-intent leads ready for AE closing.
                </p>
              </div>
            </div>
          </div>

          {/* AI Recommendations & Human-in-the-Loop */}
          <div className="p-6 rounded-2xl bg-slate-900/80 border border-slate-800 space-y-5">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Bot className="w-5 h-5 text-blue-400" />
                <h2 className="text-lg font-bold text-white">Human-In-The-Loop Approvals</h2>
              </div>
              <span className="text-xs px-2 py-0.5 rounded bg-amber-500/10 text-amber-300 border border-amber-500/20 font-medium">
                Decision Required
              </span>
            </div>

            <p className="text-xs text-slate-400">
              The AI Engine formulates actions but pauses execution until an authorized human approves sensitive operations.
            </p>

            <div className="space-y-4">
              {recommendations.map((rec) => (
                <div key={rec.id} className="p-4 rounded-xl bg-slate-950/70 border border-slate-800 space-y-3">
                  <div className="flex items-start justify-between gap-3">
                    <h3 className="font-semibold text-sm text-white">{rec.title}</h3>
                    <span className={`text-[10px] uppercase font-bold px-2 py-0.5 rounded border ${
                      rec.risk === "HIGH"
                        ? "bg-red-500/10 text-red-400 border-red-500/20"
                        : "bg-amber-500/10 text-amber-400 border-amber-500/20"
                    }`}>
                      {rec.risk} Risk
                    </span>
                  </div>

                  <p className="text-xs text-slate-400">{rec.desc}</p>

                  <div className="flex items-center justify-between pt-2 border-t border-slate-800/80">
                    <span className="text-xs font-semibold text-emerald-400">
                      Expected ROI: {rec.roi}
                    </span>

                    {rec.status === "pending" ? (
                      <div className="flex items-center gap-2">
                        <button
                          onClick={() => handleDecision(rec.id, "dismissed")}
                          className="px-2.5 py-1 text-xs font-medium rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition"
                        >
                          Dismiss
                        </button>
                        <button
                          onClick={() => handleDecision(rec.id, "approved")}
                          className="px-3 py-1 text-xs font-semibold rounded-lg bg-blue-600 hover:bg-blue-500 text-white shadow-md shadow-blue-500/20 transition flex items-center gap-1.5"
                        >
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          Approve Action
                        </button>
                      </div>
                    ) : rec.status === "approved" ? (
                      <span className="text-xs font-medium text-emerald-400 flex items-center gap-1">
                        <CheckCircle2 className="w-3.5 h-3.5" /> Approved & Dispatched via n8n
                      </span>
                    ) : (
                      <span className="text-xs font-medium text-slate-500 flex items-center gap-1">
                        <XCircle className="w-3.5 h-3.5" /> Action Dismissed
                      </span>
                    )}
                  </div>
                </div>
              ))}
            </div>

            {/* Measurable Impact Tracker */}
            <div className="mt-6 pt-5 border-t border-slate-800">
              <h4 className="text-xs font-bold text-slate-300 uppercase tracking-wider mb-3">
                Measurable Business ROI
              </h4>
              <div className="grid grid-cols-3 gap-3 text-center">
                <div className="p-2.5 rounded-lg bg-slate-950 border border-slate-800/60">
                  <div className="text-lg font-bold text-white">2,410 hrs</div>
                  <div className="text-[11px] text-slate-400">Hours Saved</div>
                </div>
                <div className="p-2.5 rounded-lg bg-slate-950 border border-slate-800/60">
                  <div className="text-lg font-bold text-emerald-400">$384,000</div>
                  <div className="text-[11px] text-slate-400">ARR Protected</div>
                </div>
                <div className="p-2.5 rounded-lg bg-slate-950 border border-slate-800/60">
                  <div className="text-lg font-bold text-blue-400">1,842</div>
                  <div className="text-[11px] text-slate-400">Tasks Automated</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-900 py-6 text-center text-xs text-slate-500 mt-auto bg-slate-950/60">
        &copy; 2026 ORVANTA AI. All Rights Reserved &bull; <span className="text-slate-400 font-semibold">Nivesh Kumar Meena</span>
      </footer>
    </div>
  );
}
