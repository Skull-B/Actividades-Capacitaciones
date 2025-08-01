import logo from './logo.svg';
import './App.css';
import Contador from '../src/Contador.jsx';
import Noti from '../src/evento.jsx';
import Todolist from '../src/ComponentesActividad/Todolist.jsx';

function App() {
  const hobbies = ['Jugar Viedeojuegos', 'Programar', 'leer Mangas y libros']
  const FOTO = 'https://th.bing.com/th/id/R.676e9734cf59f779e5236562c6dcf5e0?rik=b4AjRIu0iYNBKw&pid=ImgRaw&r=0';
  const año = new Date().getFullYear();
  return (
    <>
    <div className="Container_App">
      <h1>Juan Jose Ortegon Saavedra</h1>
      <img src={FOTO} className="App-FOTO" alt="FOTO" />
      <p>
        Soy estudiante proceso de formacion del sena ADSO, me gusta aprender cosas nuevas y disfrutar de los videojuegos.
      </p>
     <h1>"Somos guerreros de nuestro mundo"</h1>
     <ul>
      {hobbies.map((hobby, index) => (
        <li key={index}>{hobby}</li>
      ))}
      </ul> 
      <p className='fecha'>{año}</p>
    </div>
    <div>
    <Contador />
    </div>
    <div>
    <Noti />
    </div>
    <div>
    <Todolist />
    </div>

    </>
  );
}

export default App;
