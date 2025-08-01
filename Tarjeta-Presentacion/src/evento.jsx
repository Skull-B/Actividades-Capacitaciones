import './App.css';
import { useState } from 'react';
import Contador from '../src/Contador.jsx';

function Noti() {
  const [visible, setVisible] = useState(false);

  return (
    <div className="Noti" style={{ textAlign: 'center' }}>
      <button onClick={() => setVisible(!visible)}>
        {visible ? 'Ocultar notificación' : 'Mostrar notificación'}
      </button>

      {visible && (
        <div className="notification">
         <Contador />
        </div>
      )}
    </div>
  );
}

export default Noti;