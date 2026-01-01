// Modulo gerado automaticamente

function processData(data) {
    return data.map(item => item * 2);
}

class DataProcessor {
    constructor() {
        this.data = [];
    }
    
    add(item) {
        this.data.push(item);
    }
    
    process() {
        return processData(this.data);
    }
}

module.exports = { DataProcessor, processData };
