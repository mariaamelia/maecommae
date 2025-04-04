import "./assets/styles/main.css";

import Aura from "@primeuix/themes/aura";
import Button from "primevue/button";
import PrimeVue from "primevue/config";
import FloatLabel from "primevue/floatlabel";
import InputText from "primevue/inputtext";
import SelectButton from "primevue/selectbutton";
import StyleClass from "primevue/styleclass";
import ToggleSwitch from "primevue/toggleswitch";
import Toolbar from "primevue/toolbar";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
 
const app = createApp(App);

app.use(PrimeVue, {
	theme: {
		preset: Aura,
		options: {
			darkModeSelector: ".p-dark",
			ripple: false,
			cssLayer:{
				ripple: false,
				name: "primevue",
				order:"tailwind-base, primevue, tailwind-utilities"
			}
		},
		ripple: false,
	},
});

app.component("Button", Button);
app.component("InputText", InputText);
app.component("FloatLabel", FloatLabel);
app.component("Toolbar", Toolbar);
app.component("ToggleSwitch", ToggleSwitch);
app.component("SelectButton", SelectButton);

app.directive("styleclass", StyleClass);
app.use(router);
app.mount("#app");
