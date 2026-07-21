"use client";

import React from "react";
import Link from "next/link";
import { LayoutDashboard, MessageSquareText, Inbox, Cpu, Layers } from "lucide-react";

export function Navbar() {
  return (
    <header className="border-b border-slate-800 bg-slate-900/60 backdrop-blur-md sticky top-0 z-50 px-6 py-3.5 flex items-center justify-between">
      <div className="flex items-center gap-3">
        <div className="h-9 w-9 rounded-xl bg-gradient-to-tr from-blue-600 via-indigo-600 to-violet-500 flex items-center justify-center font-bold text-white shadow-lg shadow-blue-500/20">
          O
        </div>
        <div>
          <span className="font-extrabold text-lg tracking-tight text-white">ORVANTA AI</span>
          <span className="ml-2 text-xs px-2 py-0.5 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/20 font-medium">Enterprise IQ</span>
        </div>
      </div>

      <nav className="flex items-center gap-1 sm:gap-2">
        <Link
          href="/dashboard"
          className="flex items-center gap-2 px-3.5 py-1.5 text-sm font-medium rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition"
        >
          <LayoutDashboard className="w-4 h-4 text-blue-400" />
          Dashboard
        </Link>
        <Link
          href="/ai-chat"
          className="flex items-center gap-2 px-3.5 py-1.5 text-sm font-medium rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition"
        >
          <MessageSquareText className="w-4 h-4 text-indigo-400" />
          AI Copilot
        </Link>
        <Link
          href="/dashboard#inbox"
          className="flex items-center gap-2 px-3.5 py-1.5 text-sm font-medium rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition"
        >
          <Inbox className="w-4 h-4 text-amber-400" />
          AI Inbox
          <span className="h-5 px-1.5 rounded-full bg-amber-500/20 text-amber-300 text-xs font-semibold flex items-center justify-center">2</span>
        </Link>
        <Link
          href="/integrations"
          className="flex items-center gap-2 px-3.5 py-1.5 text-sm font-medium rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition"
        >
          <Layers className="w-4 h-4 text-emerald-400" />
          Integrations
        </Link>
      </nav>

      <div className="flex items-center gap-3">
        <div className="flex items-center gap-2 text-xs text-slate-400">
          <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse"></span>
          LangGraph Active
        </div>
        <div className="h-8 w-8 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-xs font-bold text-slate-300">
          EX
        </div>
      </div>
    </header>
  );
}
