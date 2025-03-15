# app/crudCateg.py

from flask import Flask, jsonify, request
import psycopg2
from app.Util.bd import connect_to_db

app = Flask(__name__)

# Endpoint para criar uma categoria
@app.route('/categories', methods=['POST'])
def create_category():
    try:
        data = request.get_json()
        category_name = data['category_name']
        description = data['description']
        picture = data['picture']

        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO categories (category_name, description, picture)
            VALUES (%s, %s, %s) RETURNING category_id;
        """, (category_name, description, picture))

        category_id = cursor.fetchone()[0]
        conn.commit()

        return jsonify({'category_id': category_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint para ler uma categoria
@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM categories WHERE category_id = %s;", (category_id,))
        category = cursor.fetchone()

        if category:
            return jsonify({
                'category_id': category[0],
                'category_name': category[1],
                'description': category[2],
                'picture': category[3]
            }), 200
        else:
            return jsonify({'error': 'Category not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint para atualizar uma categoria
@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    try:
        data = request.get_json()
        category_name = data['category_name']
        description = data['description']
        picture = data['picture']

        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE categories
            SET category_name = %s, description = %s, picture = %s
            WHERE category_id = %s;
        """, (category_name, description, picture, category_id))

        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({'error': 'Category not found'}), 404

        return jsonify({'message': 'Category updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoint para deletar uma categoria
@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM categories WHERE category_id = %s;", (category_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({'error': 'Category not found'}), 404

        return jsonify({'message': 'Category deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
