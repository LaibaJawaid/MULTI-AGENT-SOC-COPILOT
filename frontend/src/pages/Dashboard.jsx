import React, { useState } from 'react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar } from 'recharts';
import { Cpu, Shield, Search, CheckCircle, Zap } from 'lucide-react';

// AI Performance Metrics (Simple Advanced Chart Data)
const efficiencyData = [
  { time: '10:00', totalAlerts: 40, aiResolved: 35 },
  { time: '11:00', totalAlerts: 65, aiResolved: 58 },
  { time: '12:00', totalAlerts: 50, aiResolved: 47 },
  { time: '13:00', totalAlerts: 85, aiResolved: 72 },
];

const capabilityData = [
  { subject: 'RAG Accuracy', A: 92, fullMark: 100 },
  { subject: 'Tool Use (MCP)', A: 88, fullMark: 100 },
  { subject: 'Triage Speed', A: 95, fullMark: 100 },
  { subject: 'Multi-Agent Logic', A: 85, fullMark: 100 },
];

export default function AISocMVP() {
  const [logs, setLogs] = useState([
    { role: 'system', text: 'AI SOC Node Active. Waiting for incoming telemetry...' }
  ]);

  // Simulate AI Pipeline Logic for Demo
  const triggerSimulation = () => {
    setLogs([
      { role: 'triage', text: '🔄 [Triage Agent]: Ingested suspicious raw log entry.' },
      { role: 'rag', text: '🔍 [Hybrid RAG]: Searching database... Found vector match & exact keyword CVE-2026.' },
      { role: 'mcp', text: '🛠️ [MCP Tool]: Triggered IP reputation check via secure client protocol.' },
      { role: 'supervisor', text: '🎯 [Supervisor]: Verdict finalized. Threat isolated autonomously.' }
    ]);
  };

  return (
    <div className="min-h-screen bg-[#0b0f19] text-slate-100 p-6 font-sans">
      
      {/* Header Bar */}
      <div className="flex justify-between items-center border-b border-slate-800 pb-4 mb-6">
        <div className="flex items-center gap-3">
          <Shield className="text-cyan-400 h-7 w-7" />
          <h1 className="text-xl font-bold tracking-wide">Agentic SOC Platform <span className="text-xs bg-cyan-500/10 text-cyan-400 px-2 py-0.5 rounded border border-cyan-500/20">AI MVP</span></h1>
        </div>
        <button 
          onClick={triggerSimulation}
          className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 font-medium text-sm rounded-lg shadow-lg shadow-cyan-500/10 transition-all">
          <Zap className="h-4 w-4" /> Simulate AI Pipeline
        </button>
      </div>

      {/* Grid Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        {/* Left & Middle Column: Main AI Operations */}
        <div className="lg:col-span-2 space-y-6">
          
          {/* AI Orchestration & LangGraph Execution View */}
          <div className="bg-[#131a2c] rounded-xl border border-slate-800 p-5 shadow-xl">
            <h3 className="text-sm font-semibold text-slate-400 uppercase tracking-wider flex items-center gap-2 mb-4">
              <Cpu className="h-4 w-4 text-cyan-400" /> LangGraph Multi-Agent Execution Flow
            </h3>
            
            <div className="bg-[#080d1a] rounded-lg p-4 font-mono text-xs space-y-3 min-h-[220px] max-h-[300px] overflow-y-auto border border-slate-900">
              {logs.map((log, index) => (
                <div key={index} className={`p-2 rounded ${
                  log.role === 'triage' ? 'text-amber-400 bg-amber-500/5' :
                  log.role === 'rag' ? 'text-purple-400 bg-purple-500/5' :
                  log.role === 'mcp' ? 'text-cyan-400 bg-cyan-500/5' :
                  log.role === 'supervisor' ? 'text-emerald-400 bg-emerald-500/5 font-bold' : 'text-slate-500'
                }`}>
                  {log.text}
                </div>
              ))}
            </div>
          </div>

          {/* Advanced Performance Charts */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            {/* Area Chart - Automation Ratio */}
            <div className="bg-[#131a2c] rounded-xl border border-slate-800 p-4">
              <h4 className="text-xs font-semibold text-slate-400 uppercase mb-3">AI Autonomy & Processing Load</h4>
              <div className="h-48">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={efficiencyData}>
                    <defs>
                      <linearGradient id="colorAlerts" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#38bdf8" stopOpacity={0.2}/>
                        <stop offset="95%" stopColor="#38bdf8" stopOpacity={0}/>
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis dataKey="time" stroke="#64748b" fontSize={11} />
                    <YAxis stroke="#64748b" fontSize={11} />
                    <Tooltip contentStyle={{ backgroundColor: '#131a2c', borderColor: '#334155' }} />
                    <Area type="monotone" dataKey="totalAlerts" stroke="#38bdf8" fillOpacity={1} fill="url(#colorAlerts)" name="Total Events" />
                    <Area type="monotone" dataKey="aiResolved" stroke="#10b981" fillOpacity={0} name="AI Autonomous Fix" />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* Radar Chart - Agent Architecture Capabilities */}
            <div className="bg-[#131a2c] rounded-xl border border-slate-800 p-4 flex flex-col items-center">
              <h4 className="text-xs font-semibold text-slate-400 uppercase w-full mb-3 text-left">Agent Matrix Evaluation</h4>
              <div className="h-48 w-full flex justify-center">
                <ResponsiveContainer width="100%" height="100%">
                  <RadarChart cx="50%" cy="50%" radius="70%" data={capabilityData}>
                    <PolarGrid stroke="#1e293b" />
                    <PolarAngleAxis dataKey="subject" stroke="#94a3b8" fontSize={10} />
                    <PolarRadiusAxis stroke="#334155" angle={30} domain={[0, 100]} fontSize={8} />
                    <Radar name="AI Stack" dataKey="A" stroke="#22d3ee" fill="#22d3ee" fillOpacity={0.3} />
                  </RadarChart>
                </ResponsiveContainer>
              </div>
            </div>

          </div>
        </div>

        {/* Right Column: Interactive Knowledge Base & Context */}
        <div className="space-y-6">
          
          {/* Hybrid RAG Context Container */}
          <div className="bg-[#131a2c] rounded-xl border border-slate-800 p-5 shadow-xl h-full flex flex-col justify-between">
            <div>
              <h3 className="text-sm font-semibold text-slate-400 uppercase tracking-wider flex items-center gap-2 mb-4">
                <Search className="h-4 w-4 text-purple-400" /> Hybrid RAG Semantic Match
              </h3>
              
              <div className="space-y-4">
                <div className="border-l-2 border-purple-500 bg-purple-500/5 p-3 rounded-r-lg">
                  <span className="text-[10px] text-purple-400 font-mono block mb-1">DENSE EMBEDDING MATCH (94.2%)</span>
                  <p className="text-xs text-slate-300">"SOP-04: If horizontal network discovery scans originate from inside corporate infrastructure, target machine configuration parameters must be evaluated..."</p>
                </div>

                <div className="border-l-2 border-cyan-500 bg-cyan-500/5 p-3 rounded-r-lg">
                  <span className="text-[10px] text-cyan-400 font-mono block mb-1">SPARSE KEYWORD MATCH (BM25)</span>
                  <p className="text-xs text-slate-300">Found explicit identifier strings: <span className="bg-slate-800 text-cyan-400 px-1 py-0.5 rounded font-mono">auth_failure</span>, <span className="bg-slate-800 text-cyan-400 px-1 py-0.5 rounded font-mono">CVE-2026-1024</span>.</p>
                </div>
              </div>
            </div>

            <div className="mt-6 pt-4 border-t border-slate-800">
              <div className="flex items-center gap-2 text-xs text-emerald-400 bg-emerald-500/10 p-3 rounded-lg border border-emerald-500/20">
                <CheckCircle className="h-4 w-4 shrink-0" />
                <span>Reranker optimization verified top context nodes before agent generation.</span>
              </div>
            </div>
          </div>

        </div>

      </div>
    </div>
  );
}
