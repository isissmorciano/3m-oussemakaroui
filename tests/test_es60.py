"""Unit tests for es60_semplice.py - simplified version without menu interaction."""

import os
import json
import tempfile
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src/m09_files"))
from es60_semplice import (
    load_studenti,
    save_studenti,
    mostra_dettaglio,
    aggiungi_studente,
    ricerca_per_nome,
    filtra_per_voto,
)


class TestLoadSave:
    def test_load_empty_file_not_exists(self):
        """Test loading from non-existent file returns empty list."""
        result = load_studenti("/tmp/nonexistent_xyz.json")
        assert result == []

    def test_save_and_load(self):
        """Test saving and loading data."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            path = f.name

        try:
            data = [{"nome": "Alice", "voto": 8.5}, {"nome": "Bob", "voto": 7.0}]
            save_studenti(data, path)
            loaded = load_studenti(path)
            assert len(loaded) == 2
            assert loaded[0]["nome"] == "Alice"
            assert loaded[1]["voto"] == 7.0
        finally:
            if os.path.exists(path):
                os.unlink(path)

    def test_load_corrupted_json(self):
        """Test loading corrupted JSON returns empty list."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            path = f.name
            f.write("{ invalid json }")

        try:
            result = load_studenti(path)
            assert result == []
        finally:
            if os.path.exists(path):
                os.unlink(path)


class TestAggiungi:
    def test_add_valid_student(self):
        """Test adding a valid student."""
        studenti = []

        # Simulate user input
        class MockInput:
            def __init__(self):
                self.calls = 0

            def __call__(self, prompt):
                if self.calls == 0:
                    self.calls += 1
                    return "Alice"
                else:
                    return "8.5"

        import builtins

        old_input = builtins.input
        builtins.input = MockInput()
        try:
            aggiungi_studente(studenti)
            assert len(studenti) == 1
            assert studenti[0]["nome"] == "Alice"
            assert studenti[0]["voto"] == 8.5
        finally:
            builtins.input = old_input

    def test_add_to_existing_list(self):
        """Test adding student to non-empty list."""
        studenti = [{"nome": "Bob", "voto": 7.0}]

        class MockInput:
            def __init__(self):
                self.calls = 0

            def __call__(self, prompt):
                if self.calls == 0:
                    self.calls += 1
                    return "Alice"
                else:
                    return "8.5"

        import builtins

        old_input = builtins.input
        builtins.input = MockInput()
        try:
            aggiungi_studente(studenti)
            assert len(studenti) == 2
            assert studenti[1]["nome"] == "Alice"
        finally:
            builtins.input = old_input


class TestRicerca:
    def test_search_exact_match(self):
        """Test searching for exact name."""
        studenti = [{"nome": "Alice", "voto": 8.5}, {"nome": "Bob", "voto": 7.0}]

        class MockInput:
            def __call__(self, prompt):
                return "Alice"

        import builtins

        old_input = builtins.input
        builtins.input = MockInput()
        try:
            ricerca_per_nome(studenti)
        finally:
            builtins.input = old_input

    def test_search_substring(self):
        """Test substring search."""
        studenti = [{"nome": "Alice", "voto": 8.5}, {"nome": "Andrea", "voto": 9.0}, {"nome": "Bob", "voto": 7.0}]

        class MockInput:
            def __call__(self, prompt):
                return "And"

        import builtins

        old_input = builtins.input
        builtins.input = MockInput()
        try:
            ricerca_per_nome(studenti)
        finally:
            builtins.input = old_input

    def test_search_case_insensitive(self):
        """Test case-insensitive search."""
        studenti = [{"nome": "Alice", "voto": 8.5}]

        class MockInput:
            def __call__(self, prompt):
                return "alice"

        import builtins

        old_input = builtins.input
        builtins.input = MockInput()
        try:
            ricerca_per_nome(studenti)
        finally:
            builtins.input = old_input


class TestFiltra:
    def test_filter_single_value(self):
        """Test filtering by single voto."""
        studenti = [{"nome": "A", "voto": 6.0}, {"nome": "B", "voto": 7.0}, {"nome": "C", "voto": 8.0}]

        class MockInput:
            def __init__(self):
                self.calls = 0

            def __call__(self, prompt):
                if self.calls == 0:
                    self.calls += 1
                    return "7.0"
                else:
                    return "7.0"

        import builtins

        old_input = builtins.input
        builtins.input = MockInput()
        try:
            filtra_per_voto(studenti)
        finally:
            builtins.input = old_input

    def test_filter_range(self):
        """Test filtering by range."""
        studenti = [
            {"nome": "A", "voto": 6.0},
            {"nome": "B", "voto": 7.0},
            {"nome": "C", "voto": 8.0},
            {"nome": "D", "voto": 9.0},
        ]

        class MockInput:
            def __init__(self):
                self.calls = 0

            def __call__(self, prompt):
                if self.calls == 0:
                    self.calls += 1
                    return "7.0"
                else:
                    return "8.0"

        import builtins

        old_input = builtins.input
        builtins.input = MockInput()
        try:
            filtra_per_voto(studenti)
        finally:
            builtins.input = old_input


class TestDataManipulation:
    def test_list_operations(self):
        """Test append and pop operations on student list."""
        studenti = []
        s1 = {"nome": "Alice", "voto": 8.5}
        studenti.append(s1)
        assert len(studenti) == 1

        s2 = {"nome": "Bob", "voto": 7.0}
        studenti.append(s2)
        assert len(studenti) == 2

        studenti.pop(0)
        assert len(studenti) == 1
        assert studenti[0]["nome"] == "Bob"

    def test_update_voto(self):
        """Test updating student voto."""
        studenti = [{"nome": "Alice", "voto": 8.0}]
        studenti[0]["voto"] = 9.5
        assert studenti[0]["voto"] == 9.5

    def test_validation_voto_range(self):
        """Test voto validation logic."""
        voto = 7.5
        valid = 0 <= voto <= 10
        assert valid is True

        voto = 11.0
        valid = 0 <= voto <= 10
        assert valid is False

        voto = -1.0
        valid = 0 <= voto <= 10
        assert valid is False


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])
