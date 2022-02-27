# Zebrands Products APP

## Instrucciones

El repositorio se encuentra almacenado en:

```bash
git clone https://github.com/gabrielomar86/zebrands-products.git
```

### Variables de Ambiente

Antes de ejecutar la aplicacion se deben establecer las siguientes variables de ambiente:

```bash
export FLASK_APP=zebrand_product.py
export FLASK_DEBUG=1
export FLASK_ENV=development
```

### Ambientes Virtuales

Para trabajar con ambientes virtuales, para este proyecto se utilizo conda y se exporta las dependencias en el archivo requirements.txt.

Para crear un ambiente virtual con conda se debe ejecutar el siguiente comando:

```bash
conda create -n zbrandEnv python=3.9
```

Para activar el ambiente virtual:

```bash
conda activate zbrandEnv
```

Una vez activado el ambiente virtual se debe instalar las dependencias enlistadas en el archivo requirements, con el siguiente comando:

```bash
pip install -r requirements.txt
```

Una vez realizado los pasos anteriores, nos resta ejecutar la aplicacion, con el siguiente comando:

```bash
flask run
```

Para ingresar los datos a la base de datos se utilizao flas-migrate, el cual nos permite tener versionamiento de los cambios de base de datos, la primera migracion creada se encuentra en el archivo f5d6aeeb9441_initial_migration.py, en donde se crea la tabla de usuarios y productos, y se insertan datos iniciales de 5 productos y los siguientes usuarios:

#### Usuarios por defecto

```bash
1. {
    username: 'admin',
    password: 'admin'
   }
   
2. {
    username: 'user',
    password: 'user'
   }
```

### Migraciones

Para trabajar con dichas migraciones es necesario instalar la dependencia Flask-Migrate, la cual nos provee los siguientes scripts:

```bash
1. flask db init (Inicializa la carpeta de migraciones, por default se encuentra en infrastructure/migrations)

2. flask db migrate -m "Initial migration." (Crea el archivo de migracion a ser ejecutado, el mismo lee cualquier cambio realizado a la estructura de base de datos, y genera un nuevo archivo con el nombre pasado como parametro y una fecha.)

3. flask db upgrade (Ejecuta las migraciones pendientes)
```

### Base de datos

Para la persistencia de datos se utiliza flask sqlAlquemy, el cual es un ORM que nos permite trabajar con base de datos basandonos en schemas, la base de datos utilizada para esta aplicacion es SQLite. La misma se crea en la raiz de la carpeta app con el nombre test2.db

#### Ejecucion docker-compose

Para la ejecucion de la aplicacion en un ambiente dockerizado, se debe ejecutar el siguiente comando:

```bash
docker-compose up --build
```

Con esto se levantara la aplicacion en un container de docker y se levantara la aplicacion en el puerto 0.0.0.0:5000.
