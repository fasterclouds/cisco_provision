import web, sys, sqlite3

render = web.template.render('templates/')

# lista de documentos permitidos
urls = (
'/', 'index',
)

app = web.application(urls, globals())

class index:
	def GET (self):
		return render.index()

	def POST(self):
		data 		= web.input()
		nombre 		= data.nombre
		apellido 	= data.apellido
		cedula 		= data.cedula
		tiempo		= data.tiempo

		file 		= open('datos.txt','a')

		file.write(nombre 	+ ', ')
		file.write(apellido	+ ', ')
		file.write(cedula	+ ', ')
		file.write(tiempo	+ '\n')

		file.close()
		
		# nueva_tabla = "CREATE TABLE agenda (id INTEGER PRIMARY KEY, nombre VARCHAR(30), apellido VARCHAR(30), cedula VARCHAR(11), tiempo INT(20));"

		cnn = sqlite3.connect("datos.db")
		cur = cnn.cursor()
		
		sql = "insert into agenda (nombre,apellido,cedula,tiempo) " \
			+ "values ('" + nombre + "', '" + apellido + "', '" + cedula + "', " + tiempo + ")"
		
		cur.execute(sql)
		
		cnn.commit()
		
		sql = "select * from agenda"
		
		cur.execute("SELECT * FROM agenda")
		for registro in cur:
			print(registro)
		
		
		cur.close()
		cnn.close()
		
		return render.index()

if __name__ == '__main__':
	sys.argv.append('8000')
	app.run()