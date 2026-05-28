import hashlib
# Essa função esconde a senha do usuário transformando ela num código irreversível
# ou seja, quem ver o banco de dados não consegue descobrir a senha original

def censura(texto):
    return hashlib.sha256(texto.encode()).hexdigest()
#(texto) → transforma "minhasenha" em bytes:  b"minhasenha"
    # sha256(...)     → transforma os bytes num código de 64 caracteres
    # .hexdigest()    → converte esse código para texto legível
    # ex: "minhasenha" → "a665a459204...7a27ae3"