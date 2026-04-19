from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_flash_messages'

@app.route('/')
def index():
    services = [
        {
            'title': 'Desarrollo Web',
            'description': 'Creamos sitios web modernos, rápidos y adaptados a tus necesidades utilizando las últimas tecnologías.',
            'icon': 'bi-code-slash'
        },
        {
            'title': 'Marketing Digital',
            'description': 'Potenciamos tu marca en internet a través de estrategias efectivas de SEO, SEM y redes sociales.',
            'icon': 'bi-megaphone'
        },
        {
            'title': 'Consultoría IT',
            'description': 'Te asesoramos en la transformación digital de tu empresa para optimizar procesos y recursos.',
            'icon': 'bi-pc-display'
        }
    ]
    return render_template('index.html', services=services)

@app.route('/contacto', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Aquí se procesaría el formulario, por ejemplo, enviando un correo o guardando en base de datos.
        flash(f'¡Gracias {name}! Hemos recibido tu mensaje y te contactaremos pronto a {email}.', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
