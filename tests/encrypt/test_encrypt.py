from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 2)
        encrypt_message(1, "mesagem")
        encrypt_message("mensagem", "mensagem")
    assert encrypt_message("mensagem", -1) == "megasnem"
    assert encrypt_message("mensagem", 2) == "megasn_em"
    assert encrypt_message("mensagem", 4) == "mega_snem"
    assert encrypt_message("mensagem", 9) == "megasnem"
    assert encrypt_message("mensagem", 3) == "nem_megas"
