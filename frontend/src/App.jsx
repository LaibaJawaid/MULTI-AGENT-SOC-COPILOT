/*
Main Layout

Sidebar

+

Topbar

+

Pages
*/

import { Routes, Route } from "react-router-dom";

import { Box } from "@mui/material";

import Sidebar from "./components/Sidebar";

import Topbar from "./components/Topbar";

import Dashboard from "./pages/Dashboard";

import Alerts from "./pages/Alerts";

import Investigation from "./pages/Investigation";

import Graph from "./pages/Graph";

import RAG from "./pages/RAG";

import Settings from "./pages/Settings";

export default function App() {

    return (

        <Box sx={{ display: "flex" }}>

            <Sidebar />

            <Box sx={{ flexGrow: 1 }}>

                <Topbar />

                <Box sx={{ mt: 10, p: 3 }}>

                    <Routes>

                        <Route

                            path="/"

                            element={<Dashboard />}

                        />

                        <Route

                            path="/alerts"

                            element={<Alerts />}

                        />

                        <Route

                            path="/investigation"

                            element={<Investigation />}

                        />

                        <Route

                            path="/graph"

                            element={<Graph />}

                        />

                        <Route

                            path="/rag"

                            element={<RAG />}

                        />

                        <Route

                            path="/settings"

                            element={<Settings />}

                        />

                    </Routes>

                </Box>

            </Box>

        </Box>

    );

}