import { createStore } from 'vuex'
import { auth } from "./modules/auth";
import { vehicles } from "./modules/vehicles";
import { articles } from "./modules/articles";
import { bikes } from "./modules/bikes";
import { feedbacks } from "./modules/feedbacks";
import {drives} from "./modules/drives";

export default createStore({
  modules: {
    vehicles: vehicles,
    articles: articles,
    bikes: bikes,
    feedbacks: feedbacks,
    drives: drives,
    auth: auth
  }
})
