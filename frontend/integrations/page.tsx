"use client";

import React, { useState } from "react";
import { Navbar } from "../components/Navbar";
import { CheckCircle2, RefreshCw, Plus, ExternalLink, ShieldCheck } from "lucide-react";

export default function IntegrationsPage() {
  const [integrations] = useState([
    {
      id: "hubspot",
      name: "HubSpot CRM",
      category: "CRM & Pipeline",
      status: "Connected",
      syncHealth: "99.8%",
      records: "14,200 deals & contacts",
      lastSync: "4 mins ago",
    },
    {
      id: "slack",
      name: "Slack Workspaces",
      category: "Notifications & Alerts",
      status: "Connected",
      syncHealth: "100%",
      records: "#growth-alerts, #exec-churn",
      lastSync: "Real-time",
    },
    {
      id: "gmail",
      name: "Google Workspace / Gmail",
      category: "Email Outreach",
      status: "Connected",
      syncHealth: "99.4%",
      records: "Executive automated drafts",
      lastSync: "12 mins ago",
    },
    {
      id: "postgres",
      name: "PostgreSQL Data Warehouse",
      category: "Core Database",
      status: "Connected",
      syncHealth: "100%",
      records: "184,500 analytics rows",
      lastSync: "Continuous streaming",
    },
    {
      id: "n8n",
      name: "n8n Automation Engine",
      category: "Workflow Automation",
      status: "Connected",
      syncHealth: "100%",
      records: "8 Active Webhook Workflows",
      lastSync: "Real-time listener",
    },
    {
      id: "qdrant",
      name: "Qdrant Vector Database",
      category: "RAG & Knowledge Base",
      status: "Connected",
      syncHealth: "100%",
      records: "3,210 embedded document chunks",
      lastSync: "Continuous vector indexing",
    },
    {
      id: "salesforce",
      name: "Salesforce CRM",
      category: "CRM & Enterprise Sales",
      status: "Available",
      syncHealth: "—",
      records: "Ready to connect",
      lastSync: "—",
    },
    {
      id: "zendesk",
      name: "Zendesk Support",
      category: "Support Tickets",
      status: "Available",
      syncHealth: "—",
      records: "Ready to connect",
      lastSync: "—",
    },
  ]);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      <Navbar />

      <main className="flex-1 max-w-7xl w-full mx-auto px-6 py-8 space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-6">
          <div>
            <h1 className="text-2xl font-bold text-white flex items-center gap-3">
              Enterprise Integration Hub
              <span className="text-xs px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-medium">
                6 Active Connectors
              </span>
            </h1>
            <p className="text-xs text-slate-400 mt-1">
              Connect external databases, CRMs, support tickets, and communication platforms to power ORVANTA AI.
            </p>
          </div>
          <button className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-medium text-xs flex items-center gap-2 transition self-start sm:self-auto">
            <Plus className="w-4 h-4" />
            Connect New Tool
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {integrations.map((item) => (
            <div
              key={item.id}
              className="p-5 rounded-2xl bg-slate-900/70 border border-slate-800 hover:border-slate-700 transition space-y-4"
            >
              <div className="flex items-start justify-between">
                <div>
                  <h3 className="font-semibold text-white text-sm">{item.name}</h3>
                  <span className="text-[11px] text-slate-400">{item.category}</span>
                </div>
                <span
                  className={`text-[10px] font-bold px-2 py-0.5 rounded-full border ${
                    item.status === "Connected"
                      ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/20"
                      : "bg-slate-800 text-slate-400 border-slate-700"
                  }`}
                >
                  {item.status}
                </span>
              </div>

              <div className="space-y-1.5 text-xs text-slate-400">
                <div className="flex justify-between">
                  <span>Data Ingested:</span>
                  <span className="text-slate-200 font-medium">{item.records}</span>
                </div>
                <div className="flex justify-between">
                  <span>Health / Uptime:</span>
                  <span className="text-emerald-400 font-medium">{item.syncHealth}</span>
                </div>
                <div className="flex justify-between">
                  <span>Last Sync:</span>
                  <span className="text-slate-300 font-mono text-[11px]">{item.lastSync}</span>
                </div>
              </div>

              <div className="pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs">
                {item.status === "Connected" ? (
                  <button className="text-blue-400 hover:text-blue-300 flex items-center gap-1 font-medium transition">
                    <RefreshCw className="w-3.5 h-3.5" /> Force Sync
                  </button>
                ) : (
                  <button className="text-slate-400 hover:text-white flex items-center gap-1 font-medium transition">
                    Configure OAuth
                  </button>
                )}
                <ExternalLink className="w-3.5 h-3.5 text-slate-500" />
              </div>
            </div>
          ))}
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-900 py-6 text-center text-xs text-slate-500 mt-auto bg-slate-950/60">
        &copy; 2026 ORVANTA AI. All Rights Reserved &bull; <span className="text-slate-400 font-semibold">Nivesh Kumar Meena</span>
      </footer>
    </div>
  );
}
