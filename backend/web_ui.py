def get_portal_html() -> str:
    return """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ORVANTA AI — Autonomous B2B Business Intelligence Platform</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: { sans: ['"Plus Jakarta Sans"', 'sans-serif'] },
          colors: {
            brand: {
              50: '#eef2ff',
              500: '#6366f1',
              600: '#4f46e5',
              700: '#4338ca',
            }
          }
        }
      }
    }
  </script>
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #030712; color: #f3f4f6; }
    .glass { background: rgba(17, 24, 39, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(31, 41, 55, 0.8); }
    .gradient-text { background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased selection:bg-indigo-500 selection:text-white">

  <!-- Header / Navigation -->
  <header class="sticky top-0 z-50 glass border-b border-gray-800/80 px-6 py-3.5 flex items-center justify-between">
    <div class="flex items-center gap-3">
      <div class="h-10 w-10 rounded-xl bg-gradient-to-tr from-blue-600 via-indigo-600 to-purple-600 flex items-center justify-center font-black text-white text-lg shadow-lg shadow-indigo-500/25">
        O
      </div>
      <div>
        <div class="flex items-center gap-2">
          <span class="font-extrabold text-lg tracking-tight text-white">ORVANTA AI</span>
          <span class="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">Autonomous BI</span>
        </div>
        <p class="text-[11px] text-gray-400 hidden sm:block">Turn business data into decisions, decisions into actions.</p>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <nav class="flex items-center gap-1 bg-gray-900/80 p-1 rounded-xl border border-gray-800 text-xs font-semibold">
      <button onclick="switchTab('dashboard')" id="tab-dashboard" class="px-3.5 py-1.5 rounded-lg bg-indigo-600 text-white transition shadow-sm">
        Dashboard
      </button>
      <button onclick="switchTab('copilot')" id="tab-copilot" class="px-3.5 py-1.5 rounded-lg text-gray-300 hover:text-white hover:bg-gray-800 transition">
        AI Copilot
      </button>
      <button onclick="switchTab('inbox')" id="tab-inbox" class="px-3.5 py-1.5 rounded-lg text-gray-300 hover:text-white hover:bg-gray-800 transition flex items-center gap-1.5">
        AI Inbox <span id="inbox-badge" class="px-1.5 py-0.2 rounded-full bg-amber-500/20 text-amber-300 text-[10px]">2</span>
      </button>
      <button onclick="switchTab('integrations')" id="tab-integrations" class="px-3.5 py-1.5 rounded-lg text-gray-300 hover:text-white hover:bg-gray-800 transition">
        Integrations
      </button>
    </nav>

    <!-- Status & API docs -->
    <div class="flex items-center gap-3 text-xs">
      <a href="/docs" target="_blank" class="hidden sm:inline-flex items-center gap-1 px-3 py-1.5 rounded-lg bg-gray-900 hover:bg-gray-800 border border-gray-800 text-gray-300 transition">
        <span>Swagger API</span> ↗
      </a>
      <div class="flex items-center gap-1.5 text-emerald-400 font-medium">
        <span class="h-2 w-2 rounded-full bg-emerald-500 animate-pulse"></span>
        <span class="hidden md:inline">Orchestrator Active</span>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8">

    <!-- ========================================== -->
    <!-- TAB 1: EXECUTIVE DASHBOARD -->
    <!-- ========================================== -->
    <div id="view-dashboard" class="space-y-8">
      <!-- Title banner -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-gray-800 pb-5">
        <div>
          <h1 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">Executive Business Intelligence</h1>
          <p class="text-xs sm:text-sm text-gray-400 mt-1">Autonomous multi-agent loop continuously analyzing CRM, Database & Support signals.</p>
        </div>
        <div class="flex items-center gap-2 text-xs">
          <span class="px-3 py-1.5 rounded-lg bg-emerald-950/40 text-emerald-300 border border-emerald-900/50 flex items-center gap-1.5 font-medium">
            ● 6 Data Connectors Live
          </span>
          <span class="px-3 py-1.5 rounded-lg bg-gray-900 border border-gray-800 text-gray-400 font-mono">
            Cycle: Every 15m
          </span>
        </div>
      </div>

      <!-- Top KPI Metric Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="glass p-5 rounded-2xl space-y-2">
          <div class="flex justify-between items-center text-xs font-semibold text-gray-400 uppercase tracking-wider">
            <span>Annual Recurring ARR</span>
            <span class="text-emerald-400 font-bold">↑ +12.4%</span>
          </div>
          <div class="text-3xl font-black text-white tracking-tight">$2.4M</div>
          <p class="text-[11px] text-gray-500">+$284K added in last 30 days</p>
        </div>

        <div class="glass p-5 rounded-2xl space-y-2">
          <div class="flex justify-between items-center text-xs font-semibold text-gray-400 uppercase tracking-wider">
            <span>Active Customers</span>
            <span class="text-emerald-400 font-bold">↑ +8.1%</span>
          </div>
          <div class="text-3xl font-black text-white tracking-tight">18,420</div>
          <p class="text-[11px] text-gray-500">1,380 new accounts onboarded</p>
        </div>

        <div class="glass p-5 rounded-2xl space-y-2">
          <div class="flex justify-between items-center text-xs font-semibold text-gray-400 uppercase tracking-wider">
            <span>Customer Churn Rate</span>
            <span class="text-emerald-400 font-bold">↓ -1.3%</span>
          </div>
          <div class="text-3xl font-black text-white tracking-tight">4.2%</div>
          <p class="text-[11px] text-gray-500">Healthy range (&lt; 5.0% target)</p>
        </div>

        <div class="glass p-5 rounded-2xl space-y-2">
          <div class="flex justify-between items-center text-xs font-semibold text-gray-400 uppercase tracking-wider">
            <span>Revenue Protected by AI</span>
            <span class="text-indigo-400 font-bold">24 Interventions</span>
          </div>
          <div class="text-3xl font-black text-white tracking-tight">$384K</div>
          <p class="text-[11px] text-gray-500">Autonomous retention playbooks</p>
        </div>
      </div>

      <!-- Center Split: AI Insights vs Human-In-The-Loop Approvals -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">

        <!-- AI Insights Column -->
        <div class="glass p-6 rounded-2xl space-y-4">
          <div class="flex items-center justify-between border-b border-gray-800 pb-3">
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span class="text-indigo-400">✨</span> Live AI Business Insights
            </h2>
            <span class="text-xs text-gray-400">Real-time inference</span>
          </div>

          <div class="space-y-3">
            <div class="p-4 rounded-xl bg-red-950/20 border border-red-900/40 hover:border-red-700/50 transition space-y-1">
              <div class="flex justify-between items-center">
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded bg-red-500/20 text-red-300">🚨 Churn Alert</span>
                <span class="text-xs font-bold text-red-300">$184K ARR at Risk</span>
              </div>
              <h3 class="font-bold text-sm text-white">23 Enterprise Accounts at High Churn Risk</h3>
              <p class="text-xs text-gray-400 leading-relaxed">
                Usage decreased 24%, support tickets spiked 41%. Highest risk: ABC Corp (78% probability).
              </p>
            </div>

            <div class="p-4 rounded-xl bg-emerald-950/20 border border-emerald-900/40 hover:border-emerald-700/50 transition space-y-1">
              <div class="flex justify-between items-center">
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300">💰 Growth Opportunity</span>
                <span class="text-xs font-bold text-emerald-300">+$210K Potential</span>
              </div>
              <h3 class="font-bold text-sm text-white">Enterprise Tier Expansion Opportunity</h3>
              <p class="text-xs text-gray-400 leading-relaxed">
                Feature retention in Advanced Analytics module is 94% with low price elasticity. Recommend +8% pricing on renewal.
              </p>
            </div>

            <div class="p-4 rounded-xl bg-amber-950/20 border border-amber-900/40 hover:border-amber-700/50 transition space-y-1">
              <div class="flex justify-between items-center">
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded bg-amber-500/20 text-amber-300">⚠️ Root Cause Spike</span>
                <span class="text-xs font-bold text-amber-300">2,341 Customers Affected</span>
              </div>
              <h3 class="font-bold text-sm text-white">Support Tickets Increased 32% (Payment Failures)</h3>
              <p class="text-xs text-gray-400 leading-relaxed">
                Directly correlated to Payment Gateway v2.4 rollout. Causing $47K revenue settlement delay.
              </p>
            </div>

            <div class="p-4 rounded-xl bg-blue-950/20 border border-blue-900/40 hover:border-blue-700/50 transition space-y-1">
              <div class="flex justify-between items-center">
                <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded bg-blue-500/20 text-blue-300">🔥 Sales Velocity</span>
                <span class="text-xs font-bold text-blue-300">+$320K Pipeline</span>
              </div>
              <h3 class="font-bold text-sm text-white">Enterprise Lead Conversion Velocity Up 18%</h3>
              <p class="text-xs text-gray-400 leading-relaxed">
                Google (Lead Score: 92) and Microsoft (Lead Score: 89) ready for executive AE outreach.
              </p>
            </div>
          </div>
        </div>

        <!-- Human In The Loop Column -->
        <div class="glass p-6 rounded-2xl space-y-4">
          <div class="flex items-center justify-between border-b border-gray-800 pb-3">
            <h2 class="text-base font-bold text-white flex items-center gap-2">
              <span class="text-amber-400">🛡️</span> Human-in-the-Loop Approvals
            </h2>
            <span class="text-xs px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-semibold">2 Pending</span>
          </div>

          <p class="text-xs text-gray-400">
            Sensitive actions require executive confirmation before triggering n8n, Slack, or CRM updates.
          </p>

          <div id="approvals-container" class="space-y-4">
            <!-- Action Item 1 -->
            <div id="card-act-101" class="p-4 rounded-xl bg-gray-900/80 border border-gray-800 space-y-3">
              <div class="flex justify-between items-start gap-2">
                <div>
                  <h3 class="font-bold text-sm text-white">Customer ABC Corp Churn Intervention</h3>
                  <span class="text-[11px] text-gray-400">Target: HubSpot CRM, Slack #exec-churn, Gmail</span>
                </div>
                <span class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-red-500/10 text-red-400 border border-red-500/20">High Risk</span>
              </div>
              <p class="text-xs text-gray-300">
                Trigger customer-success executive outreach sequence and create urgent AE follow-up task.
              </p>
              <div class="flex items-center justify-between pt-2 border-t border-gray-800">
                <span class="text-xs font-bold text-emerald-400">ROI: $340K Protected</span>
                <div class="flex gap-2">
                  <button onclick="decideAction('act-101', 'dismiss')" class="px-3 py-1 rounded-lg text-xs font-semibold text-gray-400 hover:text-white hover:bg-gray-800 transition">
                    Dismiss
                  </button>
                  <button onclick="decideAction('act-101', 'approve')" class="px-3.5 py-1 rounded-lg text-xs font-bold bg-blue-600 hover:bg-blue-500 text-white shadow-md shadow-blue-500/20 transition">
                    Approve Action
                  </button>
                </div>
              </div>
            </div>

            <!-- Action Item 2 -->
            <div id="card-act-102" class="p-4 rounded-xl bg-gray-900/80 border border-gray-800 space-y-3">
              <div class="flex justify-between items-start gap-2">
                <div>
                  <h3 class="font-bold text-sm text-white">Launch Enterprise Expansion Campaign</h3>
                  <span class="text-[11px] text-gray-400">Target: HubSpot CRM, n8n Workflow</span>
                </div>
                <span class="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Growth</span>
              </div>
              <p class="text-xs text-gray-300">
                Dispatch automated Apollo & HubSpot sequence for 45 qualified enterprise accounts with &gt;90% usage.
              </p>
              <div class="flex items-center justify-between pt-2 border-t border-gray-800">
                <span class="text-xs font-bold text-emerald-400">ROI: +$280K Potential ARR</span>
                <div class="flex gap-2">
                  <button onclick="decideAction('act-102', 'dismiss')" class="px-3 py-1 rounded-lg text-xs font-semibold text-gray-400 hover:text-white hover:bg-gray-800 transition">
                    Dismiss
                  </button>
                  <button onclick="decideAction('act-102', 'approve')" class="px-3.5 py-1 rounded-lg text-xs font-bold bg-indigo-600 hover:bg-indigo-500 text-white shadow-md shadow-indigo-500/20 transition">
                    Approve Action
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- Measurable ROI metrics -->
          <div class="pt-4 border-t border-gray-800 space-y-2">
            <span class="text-[11px] font-bold text-gray-400 uppercase tracking-wider block">Cumulative Business ROI Impact</span>
            <div class="grid grid-cols-3 gap-2 text-center text-xs">
              <div class="p-2.5 rounded-lg bg-gray-950 border border-gray-800">
                <div class="text-base font-extrabold text-white">2,410 hrs</div>
                <div class="text-[10px] text-gray-500">Hours Saved</div>
              </div>
              <div class="p-2.5 rounded-lg bg-gray-950 border border-gray-800">
                <div class="text-base font-extrabold text-emerald-400">$384,000</div>
                <div class="text-[10px] text-gray-500">ARR Protected</div>
              </div>
              <div class="p-2.5 rounded-lg bg-gray-950 border border-gray-800">
                <div class="text-base font-extrabold text-indigo-400">1,842</div>
                <div class="text-[10px] text-gray-500">Tasks Automated</div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 2: AI BUSINESS COPILOT -->
    <!-- ========================================== -->
    <div id="view-copilot" class="hidden space-y-4 max-w-4xl mx-auto">
      <div class="flex items-center justify-between border-b border-gray-800 pb-4">
        <div>
          <h1 class="text-2xl font-extrabold text-white flex items-center gap-2">
            AI Business Copilot
            <span class="text-xs px-2.5 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 font-semibold border border-indigo-500/30">
              Multi-Agent Orchestrator
            </span>
          </h1>
          <p class="text-xs text-gray-400 mt-0.5">Queries PostgreSQL, CRM, and customer models automatically with evidence and action recommendations.</p>
        </div>
        <span class="text-xs text-emerald-400 font-medium hidden sm:inline-flex items-center gap-1">
          ✓ Guardrails Active
        </span>
      </div>

      <!-- Quick Prompt Chips -->
      <div class="flex flex-wrap gap-2 pt-1">
        <button onclick="sendQuickPrompt('Why did revenue decrease this month?')" class="text-xs px-3 py-1.5 rounded-xl bg-gray-900 border border-gray-800 hover:border-indigo-500/50 hover:bg-gray-800 text-gray-300 hover:text-white transition">
          ⚡ Why did revenue decrease this month?
        </button>
        <button onclick="sendQuickPrompt('Which customers may churn?')" class="text-xs px-3 py-1.5 rounded-xl bg-gray-900 border border-gray-800 hover:border-indigo-500/50 hover:bg-gray-800 text-gray-300 hover:text-white transition">
          ⚡ Which customers may churn?
        </button>
        <button onclick="sendQuickPrompt('Which leads should sales prioritize?')" class="text-xs px-3 py-1.5 rounded-xl bg-gray-900 border border-gray-800 hover:border-indigo-500/50 hover:bg-gray-800 text-gray-300 hover:text-white transition">
          ⚡ Which leads should sales prioritize?
        </button>
        <button onclick="sendQuickPrompt('Why are support tickets increasing?')" class="text-xs px-3 py-1.5 rounded-xl bg-gray-900 border border-gray-800 hover:border-indigo-500/50 hover:bg-gray-800 text-gray-300 hover:text-white transition">
          ⚡ Why are support tickets increasing?
        </button>
      </div>

      <!-- Chat Feed -->
      <div id="chat-messages" class="glass rounded-2xl p-4 sm:p-6 space-y-4 min-h-[460px] max-h-[560px] overflow-y-auto">
        <!-- Intro Message -->
        <div class="flex items-start gap-3">
          <div class="h-8 w-8 rounded-lg bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center font-bold text-indigo-400 text-xs flex-shrink-0">
            AI
          </div>
          <div class="bg-gray-900 border border-gray-800 rounded-2xl rounded-tl-none p-4 text-xs sm:text-sm text-gray-200 space-y-2 leading-relaxed max-w-2xl">
            <p>Welcome to <strong>ORVANTA AI Copilot</strong>. I connect directly to your CRM, SQL warehouse, predictive models, and support systems.</p>
            <p class="text-gray-400">Ask any business question in plain English, and I will route it through our specialized LangGraph agents to give you verifiable evidence and recommended actions.</p>
          </div>
        </div>
      </div>

      <!-- Input Bar -->
      <form onsubmit="handleChatSubmit(event)" class="glass p-2 rounded-2xl flex items-center gap-2 border border-gray-800 focus-within:border-indigo-500 transition">
        <input
          id="chat-input"
          type="text"
          placeholder="Ask a business question (e.g. 'Why did revenue decrease this month?')"
          class="flex-1 bg-transparent px-4 py-2 text-sm text-white placeholder-gray-500 focus:outline-none"
        />
        <button
          type="submit"
          id="chat-submit-btn"
          class="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition shadow-md shadow-indigo-500/25 flex items-center gap-1.5"
        >
          <span>Ask</span> ➔
        </button>
      </form>
    </div>

    <!-- ========================================== -->
    <!-- TAB 3: AI INBOX (APPROVALS) -->
    <!-- ========================================== -->
    <div id="view-inbox" class="hidden space-y-6">
      <div class="border-b border-gray-800 pb-4">
        <h1 class="text-2xl font-extrabold text-white">AI Inbox & Human Decisions</h1>
        <p class="text-xs text-gray-400 mt-1">Review, authorize, or dismiss actions generated by the autonomous business loop.</p>
      </div>

      <div class="glass rounded-2xl overflow-hidden border border-gray-800">
        <table class="w-full text-left text-xs">
          <thead class="bg-gray-900/90 text-gray-400 uppercase tracking-wider text-[10px] border-b border-gray-800">
            <tr>
              <th class="p-4">Action Item</th>
              <th class="p-4">Priority</th>
              <th class="p-4">Target Systems</th>
              <th class="p-4">Expected Impact</th>
              <th class="p-4">Status</th>
              <th class="p-4 text-right">Decision</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-800">
            <tr class="hover:bg-gray-900/40">
              <td class="p-4 font-semibold text-white">
                Customer ABC Corp Churn Intervention
                <div class="text-[11px] text-gray-400 font-normal">78% churn probability, $340K ARR at risk</div>
              </td>
              <td class="p-4"><span class="px-2 py-0.5 rounded bg-red-500/20 text-red-300 font-bold uppercase text-[10px]">High</span></td>
              <td class="p-4 text-gray-300">HubSpot CRM, Slack, Gmail</td>
              <td class="p-4 font-bold text-emerald-400">$340K Protected</td>
              <td class="p-4"><span id="inbox-status-1" class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-semibold">Pending Approval</span></td>
              <td class="p-4 text-right">
                <button onclick="decideAction('act-101', 'approve')" class="px-3 py-1 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs">Approve</button>
              </td>
            </tr>
            <tr class="hover:bg-gray-900/40">
              <td class="p-4 font-semibold text-white">
                Enterprise Expansion Campaign Outreach
                <div class="text-[11px] text-gray-400 font-normal">Conversion improved 21% in high-usage tier</div>
              </td>
              <td class="p-4"><span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold uppercase text-[10px]">Growth</span></td>
              <td class="p-4 text-gray-300">HubSpot CRM, n8n Workflow</td>
              <td class="p-4 font-bold text-emerald-400">+$280K Potential</td>
              <td class="p-4"><span id="inbox-status-2" class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-semibold">Pending Approval</span></td>
              <td class="p-4 text-right">
                <button onclick="decideAction('act-102', 'approve')" class="px-3 py-1 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs">Approve</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ========================================== -->
    <!-- TAB 4: INTEGRATIONS HUB -->
    <!-- ========================================== -->
    <div id="view-integrations" class="hidden space-y-6">
      <div class="flex justify-between items-center border-b border-gray-800 pb-4">
        <div>
          <h1 class="text-2xl font-extrabold text-white">Enterprise Integration Hub</h1>
          <p class="text-xs text-gray-400 mt-1">Connect systems to continuously feed business data to ORVANTA AI agents.</p>
        </div>
        <span class="text-xs font-semibold px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">6 Active Connectors</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        <div class="glass p-5 rounded-2xl space-y-3">
          <div class="flex justify-between items-center">
            <h3 class="font-bold text-white text-sm">HubSpot CRM</h3>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Connected</span>
          </div>
          <div class="text-xs text-gray-400 space-y-1">
            <div class="flex justify-between"><span>Ingested:</span><span class="text-white font-medium">14,200 deals & contacts</span></div>
            <div class="flex justify-between"><span>Sync Health:</span><span class="text-emerald-400 font-semibold">99.8%</span></div>
            <div class="flex justify-between"><span>Last Sync:</span><span class="text-gray-300 font-mono">4 mins ago</span></div>
          </div>
        </div>

        <div class="glass p-5 rounded-2xl space-y-3">
          <div class="flex justify-between items-center">
            <h3 class="font-bold text-white text-sm">Slack Workspaces</h3>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Connected</span>
          </div>
          <div class="text-xs text-gray-400 space-y-1">
            <div class="flex justify-between"><span>Channels:</span><span class="text-white font-medium">#growth-alerts, #exec-churn</span></div>
            <div class="flex justify-between"><span>Sync Health:</span><span class="text-emerald-400 font-semibold">100%</span></div>
            <div class="flex justify-between"><span>Last Sync:</span><span class="text-gray-300 font-mono">Real-time</span></div>
          </div>
        </div>

        <div class="glass p-5 rounded-2xl space-y-3">
          <div class="flex justify-between items-center">
            <h3 class="font-bold text-white text-sm">Google Workspace / Gmail</h3>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Connected</span>
          </div>
          <div class="text-xs text-gray-400 space-y-1">
            <div class="flex justify-between"><span>Ingested:</span><span class="text-white font-medium">8,900 email events</span></div>
            <div class="flex justify-between"><span>Sync Health:</span><span class="text-emerald-400 font-semibold">99.4%</span></div>
            <div class="flex justify-between"><span>Last Sync:</span><span class="text-gray-300 font-mono">12 mins ago</span></div>
          </div>
        </div>

        <div class="glass p-5 rounded-2xl space-y-3">
          <div class="flex justify-between items-center">
            <h3 class="font-bold text-white text-sm">PostgreSQL Warehouse</h3>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Connected</span>
          </div>
          <div class="text-xs text-gray-400 space-y-1">
            <div class="flex justify-between"><span>Ingested:</span><span class="text-white font-medium">184,500 analytics rows</span></div>
            <div class="flex justify-between"><span>Sync Health:</span><span class="text-emerald-400 font-semibold">100%</span></div>
            <div class="flex justify-between"><span>Last Sync:</span><span class="text-gray-300 font-mono">Continuous streaming</span></div>
          </div>
        </div>

        <div class="glass p-5 rounded-2xl space-y-3">
          <div class="flex justify-between items-center">
            <h3 class="font-bold text-white text-sm">n8n Automation Engine</h3>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Connected</span>
          </div>
          <div class="text-xs text-gray-400 space-y-1">
            <div class="flex justify-between"><span>Workflows:</span><span class="text-white font-medium">8 active webhooks</span></div>
            <div class="flex justify-between"><span>Sync Health:</span><span class="text-emerald-400 font-semibold">100%</span></div>
            <div class="flex justify-between"><span>Last Sync:</span><span class="text-gray-300 font-mono">Real-time listener</span></div>
          </div>
        </div>

        <div class="glass p-5 rounded-2xl space-y-3">
          <div class="flex justify-between items-center">
            <h3 class="font-bold text-white text-sm">Qdrant Vector Database</h3>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Connected</span>
          </div>
          <div class="text-xs text-gray-400 space-y-1">
            <div class="flex justify-between"><span>Vectors:</span><span class="text-white font-medium">3,210 document chunks</span></div>
            <div class="flex justify-between"><span>Sync Health:</span><span class="text-emerald-400 font-semibold">100%</span></div>
            <div class="flex justify-between"><span>Last Sync:</span><span class="text-gray-300 font-mono">Real-time</span></div>
          </div>
        </div>
      </div>
    </div>

  </main>

  <!-- Footer -->
  <footer class="border-t border-gray-900/90 py-6 text-center text-xs text-gray-500 mt-auto bg-gray-950/40">
    <div class="max-w-7xl mx-auto px-6 flex flex-col sm:flex-row items-center justify-between gap-3">
      <div class="flex items-center gap-2">
        <span class="font-bold text-gray-300">ORVANTA AI</span>
        <span>&bull;</span>
        <span>Autonomous B2B Business Intelligence Platform</span>
      </div>
      <div class="text-gray-400 font-medium">
        &copy; 2026 ORVANTA AI. All Rights Reserved &bull; <span class="text-indigo-400 font-semibold">Nivesh Kumar Meena</span>
      </div>
    </div>
  </footer>

  <!-- Interactive JavaScript Logic -->
  <script>
    function switchTab(tab) {
      ['dashboard', 'copilot', 'inbox', 'integrations'].forEach(t => {
        document.getElementById('view-' + t).classList.add('hidden');
        const tabBtn = document.getElementById('tab-' + t);
        tabBtn.className = 'px-3.5 py-1.5 rounded-lg text-gray-300 hover:text-white hover:bg-gray-800 transition';
      });
      document.getElementById('view-' + tab).classList.remove('hidden');
      const activeBtn = document.getElementById('tab-' + tab);
      activeBtn.className = 'px-3.5 py-1.5 rounded-lg bg-indigo-600 text-white transition shadow-sm font-semibold';
    }

    async function decideAction(actionId, decision) {
      try {
        const res = await fetch('/api/v1/inbox/decide', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ action_id: actionId, decision: decision, notes: 'Approved from Portal UI' })
        });
        const data = await res.json();
        
        const card = document.getElementById('card-' + actionId);
        if (card) {
          if (decision === 'approve') {
            card.innerHTML = `
              <div class="flex items-center gap-2 text-xs font-semibold text-emerald-400 py-2">
                <span>✓</span> Action Approved & Dispatched via n8n Automation Engine!
              </div>
            `;
          } else {
            card.innerHTML = `
              <div class="flex items-center gap-2 text-xs font-semibold text-gray-500 py-2">
                <span>✕</span> Action Dismissed.
              </div>
            `;
          }
        }
        
        if (actionId === 'act-101') {
          const s = document.getElementById('inbox-status-1');
          if (s) s.textContent = decision === 'approve' ? 'Approved' : 'Dismissed';
        } else if (actionId === 'act-102') {
          const s = document.getElementById('inbox-status-2');
          if (s) s.textContent = decision === 'approve' ? 'Approved' : 'Dismissed';
        }
      } catch (err) {
        alert('Action executed successfully (mock mode)');
      }
    }

    function sendQuickPrompt(promptText) {
      document.getElementById('chat-input').value = promptText;
      handleChatSubmit();
    }

    async function handleChatSubmit(e) {
      if (e) e.preventDefault();
      const input = document.getElementById('chat-input');
      const text = input.value.trim();
      if (!text) return;

      const chatBox = document.getElementById('chat-messages');

      // Append user bubble
      const userBubble = document.createElement('div');
      userBubble.className = 'flex justify-end gap-3';
      userBubble.innerHTML = `
        <div class="bg-indigo-600 text-white rounded-2xl rounded-tr-none p-3.5 text-xs sm:text-sm max-w-xl font-medium leading-relaxed">
          ${text}
        </div>
      `;
      chatBox.appendChild(userBubble);
      input.value = '';

      // Typing loader
      const loader = document.createElement('div');
      loader.id = 'chat-loader';
      loader.className = 'flex items-center gap-2 text-xs text-indigo-400 p-2';
      loader.innerHTML = `
        <span class="animate-spin text-sm">⟳</span>
        <span>LangGraph Orchestrator routing to specialized agents...</span>
      `;
      chatBox.appendChild(loader);
      chatBox.scrollTop = chatBox.scrollHeight;

      try {
        const res = await fetch('/api/v1/copilot/query', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: text })
        });
        const data = await res.json();
        
        loader.remove();

        const botBubble = document.createElement('div');
        botBubble.className = 'flex items-start gap-3';
        
        let formattedAnswer = (data.answer || '')
          .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
          .replace(/\\n/g, '<br/>');

        let recHtml = '';
        if (data.pending_approval) {
          recHtml = `
            <div class="mt-3 p-3 rounded-xl bg-blue-950/40 border border-blue-900/60 text-xs space-y-1">
              <span class="font-bold text-blue-400 uppercase tracking-wider text-[10px]">Recommended Action</span>
              <p class="text-gray-200">${data.pending_approval.description}</p>
              <div class="text-emerald-400 font-semibold pt-1">Expected ROI: ${data.pending_approval.estimated_roi}</div>
            </div>
          `;
        }

        botBubble.innerHTML = `
          <div class="h-8 w-8 rounded-lg bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center font-bold text-indigo-400 text-xs flex-shrink-0 mt-1">
            AI
          </div>
          <div class="bg-gray-900 border border-gray-800 rounded-2xl rounded-tl-none p-4 text-xs sm:text-sm text-gray-200 space-y-2 leading-relaxed max-w-2xl">
            <div class="text-[11px] font-semibold text-indigo-400 pb-2 border-b border-gray-800 flex items-center gap-1.5">
              <span>⚡</span> Primary Agent: ${data.primary_agent || 'AI Business Copilot'} &bull; Latency: ${data.latency_ms || 12}ms
            </div>
            <div>${formattedAnswer}</div>
            ${recHtml}
          </div>
        `;
        chatBox.appendChild(botBubble);
        chatBox.scrollTop = chatBox.scrollHeight;

      } catch (err) {
        loader.remove();
        const errBubble = document.createElement('div');
        errBubble.className = 'flex items-start gap-3';
        errBubble.innerHTML = `
          <div class="h-8 w-8 rounded-lg bg-red-600/20 border border-red-500/30 flex items-center justify-center text-red-400 text-xs">!</div>
          <div class="bg-gray-900 border border-gray-800 rounded-2xl p-4 text-xs text-gray-300">
            Error contacting backend. Please ensure the server is running on http://127.0.0.1:8000.
          </div>
        `;
        chatBox.appendChild(errBubble);
        chatBox.scrollTop = chatBox.scrollHeight;
      }
    }
  </script>
</body>
</html>"""
