/*
Professional SOC Theme

Dark Blue Theme

No fancy colors.

Looks similar to
Microsoft Sentinel,
CrowdStrike,
Elastic,
Splunk.
*/

import { createTheme } from "@mui/material/styles";

const theme = createTheme({

    palette: {

        mode: "dark",

        primary: {

            main: "#00B8D9"

        },

        secondary: {

            main: "#4CAF50"

        },

        background: {

            default: "#0F172A",

            paper: "#1E293B"

        }

    }

});

export default theme;