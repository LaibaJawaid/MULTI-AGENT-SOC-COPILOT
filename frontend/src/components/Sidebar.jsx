/*
Professional Sidebar

Every page
is accessible here.
*/

import { Drawer, List, ListItemButton, ListItemText } from "@mui/material";

import { Link } from "react-router-dom";

const menu = [

    ["Dashboard", "/"],

    ["Alerts", "/alerts"],

    ["Investigation", "/investigation"],

    ["Knowledge Graph", "/graph"],

    ["Hybrid RAG", "/rag"],

    ["Settings", "/settings"]

];

export default function Sidebar() {

    return (

        <Drawer

            variant="permanent"

            sx={{

                width: 240,

                "& .MuiDrawer-paper": {

                    width: 240

                }

            }}

        >

            <List>

                {

                    menu.map(item => (

                        <ListItemButton

                            component={Link}

                            to={item[1]}

                            key={item[0]}

                        >

                            <ListItemText

                                primary={item[0]}

                            />

                        </ListItemButton>

                    ))

                }

            </List>

        </Drawer>

    );

}