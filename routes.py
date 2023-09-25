from flask import Blueprint, render_template, session, redirect, request, flash, url_for
from flask_login import current_user
import forms
from api.produto import ProdutoClient
from api.usuario import UserClient
from api.carrinho import CarrinhoClient

blueprint = Blueprint('store-frontend', __name__)


@blueprint.context_processor
def cart_count():
    count = 0
    carrinho = session.get('carrinho')
    if carrinho:
        for item in carrinho.get('carrinho_items'):
            count += item['quantity']

    return {'cart_items': count}


@blueprint.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated:
        session['carrinho'] = CarrinhoClient.get_carrinho_from_session()
    try:
        produtos = ProdutoClient.get_produtos()
    except:
        produtos = {'result': []}

    return render_template('index.html', produtos=produtos)


@blueprint.route('/cadastro', methods=['POST', 'GET'])
def register():
    form = forms.RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data

            if UserClient.user_exists(username):
                flash("Por favor tente outro usuário!")
                return render_template('cadastro.html', form=form)
            else:
                response = UserClient.create_user(form)
                response_json = response.json();
                print(response_json)
                if response_json['status'] == '400': 
                    flash(response_json['message'])
                    return render_template('cadastro.html', form=form)
                user = response_json
                if user:
                    flash("Registrado. Por favor digite o login.")
                    return redirect(url_for('store-frontend.index'))
        else:
            flash("Errors")

    return render_template('cadastro.html', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            api_key = UserClient.login(form)
            if api_key:
                session['user_api_key'] = api_key
                user = UserClient.get_user()
                session['user'] = user['result']

                carrinho = CarrinhoClient.get_carrinho()
                if carrinho.get('result'):
                    session['carrinho'] = carrinho['result']

                flash('Bem vindo novamente!')
                return redirect(url_for('store-frontend.index'))
            else:
                flash('Não pode logar!!!')
        else:
            flash('Não pode logar!!!')

    return render_template('login.html', form=form)


@blueprint.route('/logout', methods=['GET'])
def logout():
    session.clear()
    flash('Logged out')
    return redirect(url_for('store-frontend.index'))


@blueprint.route('/produtos/<slug>', methods=['GET', 'POST'])
def produto_details(slug):
    response = ProdutoClient.get_produto(slug)
    produto = response['result']

    form = forms.ItemForm(produto_id=produto['id'])

    if request.method == 'POST':
        if 'user' not in session:
            flash("Por favor logar no sistema!!!")
            return redirect(url_for('store-frontend.login'))

        carrinho = CarrinhoClient.add_to_cart(produto_id=produto['id'], quantity=1)
        print(carrinho)
        session['carrinho'] = carrinho['result']
        flash("Produto adicionado a esse carrinho")

    return render_template('produto_info.html', produto=produto, form=form)


@blueprint.route('/checkout', methods=['GET'])
def checkout():
    if 'user' not in session:
        flash('Por favor logue')
        return redirect(url_for('store-frontend.login'))

    if 'carrinho' not in session:
        flash("Por favor adicione alguns produtos ao carrinho")
        return redirect(url_for("store-frontend.index"))

    carrinho = CarrinhoClient.get_carrinho()

    if len(carrinho['result']['carrinho_items']) == 0:
        flash("Favor adicione alguns itens para o carrinho!!!")
        return redirect(url_for("store-frontend.index"))

    CarrinhoClient.checkout()

    return redirect(url_for('store-frontend.obrigado'))


@blueprint.route('/obrigado', methods=['GET'])
def obrigado():
    if 'user' not in session:
        flash('Por favor logue na aplicação')
        return redirect(url_for('store-frontend.login'))

    if 'carrinho' not in session:
        flash("Favor adicione alguns itens ao carrinho")
        return redirect(url_for("store-frontend.index"))

    session.pop('carrinho', None)
    flash("Sua compra está processando!!")

    return render_template('obrigado.html')
