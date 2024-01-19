import { Switch, Route } from "react-router-dom";
import Header from './components/Header';
import Hero from "./components/Hero";
import Home from "./components/Home";
import HeroPowerForm from "./components/HeroPowerForm";
import Power from "./components/Power";
import PowerEditForm from "./components/PowerEditForm";

function App() {
  return (
    <div>
      <Header />
      <main>
          <Route exact path="/hero_powers/new">
            <HeroPowerForm />
          </Route>
          <Route exact path="/powers/:id/edit">
            <PowerEditForm />
          </Route>
          <Route exact path="/powers/:id">
            <Power />
          </Route>
          <Route exact path="/heroes/:id">
            <Hero />
          </Route>
          <Route exact path="/">
            <Home />
          </Route>
    
      </main>
    </div>
  );
}

export default App;
