#!/usr/bin/env python3
"""Modulo gerado automaticamente"""

def process_data(data):
    """Processa dados"""
    result = []
    for item in data:
        result.append(item * 2)
    return result

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def add(self, item):
        self.data.append(item)
    
    def process(self):
        return process_data(self.data)

if __name__ == "__main__":
    processor = DataProcessor()
    print("Processador inicializado")
