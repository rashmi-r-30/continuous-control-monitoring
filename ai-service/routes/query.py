from flask import Blueprint, request, jsonify
from services.groq_client import GroqClient
from services.chroma_client import ChromaClient
from services.redis_cache import RedisCache
from services.cache_instance import cache

query_bp = Blueprint("query", __name__)

groq = GroqClient()
chroma = ChromaClient()

@query_bp.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()

        if not data or "question" not in data:
            return jsonify({"error": "Please provide 'question'"}), 400

        question = data["question"].strip()

        if not question:
            return jsonify({"error": "Question cannot be empty"}), 400


        skip_cache = data.get("skip_cache", False)

        cached = None

        if not skip_cache:
            cached = cache.get(question)

        if cached:
            return jsonify({
                "answer": cached["answer"],
                "sources": cached["sources"],
                "cached": True
            })


        sources = chroma.collection.query(
            query_texts=[question],
            n_results=3
        )["documents"][0]

        context = "\n".join(sources)

        prompt = f"""
You are a professional AI assistant.

Use ONLY the provided context.
If context is insufficient, clearly say so.

Answer in concise bullet points or short paragraphs.

Context:
{context}

Question:
{question}
"""

        answer = groq.generate_text(prompt)


        cache.set(question, {
            "answer": answer,
            "sources": sources
        })


        return jsonify({
            "answer": answer,
            "sources": sources,
            "cached": False
        })

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500