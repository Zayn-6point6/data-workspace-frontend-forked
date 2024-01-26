// @ts-nocheck
import {
  BrowserRouter as BrowserRouter,
  Route,
  Routes
} from 'react-router-dom';

import { createStore } from 'little-state-machine';
import { createStore, StateMachineProvider } from 'little-state-machine';

import Confirmation from './Confirmation';
import Contact from './Contact';
import Feedback from './Feedback';

const initialState = {
  contact: {
    firstName: '',
    lastName: '',
    message: '',
    feedback: 'no',
    feedbackMessage: ''
  }
};

createStore(initialState);

export default function App() {
  return (
    <StateMachineProvider>
      <BrowserRouter basename="/support-and-feedback">
        <Routes>
          <Route exact path="/" element={<Contact />} />
          <Route path="/feedback" element={<Feedback />} />
          <Route path="/confirmation" element={<Confirmation />} />
        </Routes>
      </BrowserRouter>
    </StateMachineProvider>
  );
}
