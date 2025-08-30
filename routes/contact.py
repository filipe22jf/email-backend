from flask import Blueprint, request, jsonify
from flask_mail import Mail, Message
import os

contact_bp = Blueprint('contact', __name__)

def init_mail(app):
    """Inicializa o Flask-Mail com as configurações"""
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'filipepwajf@gmail.com')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME', 'filipepwajf@gmail.com')
    
    mail = Mail(app)
    return mail

@contact_bp.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        required_fields = ['name', 'email', 'project', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Campo {field} é obrigatório'}), 400
        
        # Criar mensagem de email
        subject = f"Novo contato do portfólio: {data['project']}"
        
        body = f"""
        Nova mensagem recebida através do portfólio PWA:
        
        Nome: {data['name']}
        Email: {data['email']}
        WhatsApp: {data.get('phone', 'Não informado')}
        Tipo de Projeto: {data['project']}
        
        Mensagem:
        {data['message']}
        
        ---
        Enviado através do formulário de contato do portfólio PWA
        """
        
        # Para desenvolvimento, vamos simular o envio
        # Em produção, você precisará configurar as credenciais do Gmail
        print("=== EMAIL SIMULADO ===")
        print(f"Para: filipepwajf@gmail.com")
        print(f"Assunto: {subject}")
        print(f"Corpo:\n{body}")
        print("=====================")
        
        return jsonify({
            'success': True,
            'message': 'Email enviado com sucesso!'
        }), 200
        
    except Exception as e:
        print(f"Erro ao enviar email: {str(e)}")
        return jsonify({
            'error': 'Erro interno do servidor',
            'message': str(e)
        }), 500

