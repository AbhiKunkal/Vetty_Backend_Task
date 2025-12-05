from flask import Blueprint

meta_bp = Blueprint('meta', __name__)

@meta_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@meta_bp.route('/version', methods=['GET'])
def version():
    return jsonify({"version": "1.0"})