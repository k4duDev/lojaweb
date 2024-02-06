from flask import render_template, session, request, redirect, url_for, flash
from loja import app, db, bcrypt
from .models import User
from .forms import RegistrationForm
import os

@app.route('/')
def home():
    return render_template('admin/index.html', title='Pagina Administrativa')


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username=form.username.data, email=form.email.data,
                password=form.password)
        db.session.add(User)
        db.session.commit()
        flash(f'Obrigado {form.name.data} por registrar','success')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Pagina de Registros")