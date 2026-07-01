/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

const { use } = require("react");

// Select the database to use.

// Adicionar aos documentos criados de itens: a lista de clientes interessados,
// vendedores parceiros e especificações técnicas, você deve decidir entre usar arrays,
// embedding (aninhamento) ou linking (referência).

use('EcommerceDB');
db.getCollection('produtos').insertMany([
  {
    "nome_item": "The Book of Concealment (Dungeons & Dragons) A Game Screen and Journal in One",
    "fabricante": "Official Dungeons & Dragons Licensed ",
    "data_lancamento": "2024-12-17",
    "preco": 110.82,
    "estoque_total": 200,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  },
  {
    "nome_item": "Wireless Noise Cancelling Headphones",
    "fabricante": "Sony",
    "data_lancamento": "2023-09-10",
    "preco": 899.99,
    "estoque_total": 150,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  },
  {
    "nome_item": "Mechanical Gaming Keyboard RGB",
    "fabricante": "Corsair",
    "data_lancamento": "2022-11-05",
    "preco": 349.90,
    "estoque_total": 80,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  },
  {
    "nome_item": "Smart LED Light Bulb",
    "fabricante": "Philips Hue",
    "data_lancamento": "2024-03-22",
    "preco": 59.99,
    "estoque_total": 500,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  },
  {
    "nome_item": "4K Ultra HD Action Camera",
    "fabricante": "GoPro",
    "data_lancamento": "2023-07-15",
    "preco": 1299.00,
    "estoque_total": 60,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  },
  {
    "nome_item": "Portable Bluetooth Speaker",
    "fabricante": "JBL",
    "data_lancamento": "2024-01-30",
    "preco": 249.50,
    "estoque_total": 220,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  },
  {
    "nome_item": "Fitness Smartwatch",
    "fabricante": "Garmin",
    "data_lancamento": "2023-05-18",
    "preco": 799.00,
    "estoque_total": 95,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  },
  {
    "nome_item": "External SSD 1TB",
    "fabricante": "Samsung",
    "data_lancamento": "2022-12-01",
    "preco": 599.99,
    "estoque_total": 130,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  },
  {
    "nome_item": "Ergonomic Office Chair",
    "fabricante": "Herman Miller",
    "data_lancamento": "2024-04-10",
    "preco": 2499.00,
    "estoque_total": 40,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  },
  {
    "nome_item": "Electric Toothbrush",
    "fabricante": "Oral-B",
    "data_lancamento": "2023-10-25",
    "preco": 199.90,
    "estoque_total": 300,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  },
  {
    "nome_item": "Smartphone Android 5G",
    "fabricante": "Samsung",
    "data_lancamento": "2024-02-14",
    "preco": 3499.00,
    "estoque_total": 75
  }
]);

// CRUD.
// Inserção: Adicione um novo item raro ao catálogo usando insertOne.
use('EcommerceDB');
db.getCollection('produtos').insertOne(
  {
    "nome_item": "CD do Jonnhy Silverhand (Cyberpunk 2077) - Edição de Colecionador",
    "fabricante": "CD Projekt Red",
    "data_lancamento": "2077-12-01",
    "preco": 999.99,
    "estoque_total": 1,
    "clientes_interessados": [],
    "vendedores_parceiros": [],
    "especificacoes_tecnicas": []
  }
);

// Consulta: Realize um find para listar produtos com preço superior a R$ 500,00.
use('EcommerceDB');
db.getCollection('produtos').find({ "preco": { $gt: 500 } });

// Atualização: Adicione um novo usuário à Fila de Espera (equivalente à Lista VIP) de
// um item específico usando updateOne.
use('EcommerceDB');
db.getCollection('produtos').updateOne(
  { 'nome_item': 'CD do Jonnhy Silverhand (Cyberpunk 2077) - Edição de Colecionador' },
  { $push: { 'clientes_interessados': 'Danton Rodrigues' } }
);

// Exclusão: Remova um item que saiu de linha utilizando deleteOne.
use('EcommerceDB');
db.getCollection('produtos').deleteOne({ 'nome_item': 'Smartphone Android 5G' });

use('EcommerceDB');
db.getCollection('produtos').find({ "nome_item": 'CD do Jonnhy Silverhand (Cyberpunk 2077) - Edição de Colecionador' });

// Lógica de Vendas e Estoque
// Simule uma venda: ao registrar um novo comprador(clientes_interessados) no documento do produto,
// utilize o updateOne para decrementar o estoque_total.
// Gerencie versões do produto (ex: Versão Padrão, Versão Deluxe, Versão de
// Colecionador) com preços diferentes dentro do mesmo documento de produto'
use('EcommerceDB');
db.getCollection('produtos').updateOne(
  { 'nome_item': 'CD do Jonnhy Silverhand (Cyberpunk 2077) - Edição de Colecionador' },
  { 
    $inc: { 'estoque_total': -1 },// incrementa o valor de um campo numérico por um valor exato especificado 
    $push: { 'clientes_interessados': 'Maria Silva 2'},
    $set: {
      versoes: [
        { nome: "Padrão", preco: 200 },
        { nome: "Deluxe", preco: 500 },
        { nome: "Colecionador", preco: 800 }
      ]
    } 
  }
);

// Collection Final deve conter, utilizando os comando de CRUD:

// Pelo menos 10 variações/versões do produto.
use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'The Book of Concealment (Dungeons & Dragons) A Game Screen and Journal in One' },
  { 
    $set: {
      versoes: [
        { nome: "Comum", preco: 200 },
        { nome: "Raro", preco: 500 }
      ]
    } 
  }
);

use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'Mechanical Gaming Keyboard RGB' },
  { 
    $set: {
      versoes: [
        { nome: "Comum", preco: 200 },
        { nome: "Rarissima", preco: 500 }
      ]
    } 
  }
);

use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'Smart LED Light Bulb' },
  { 
    $set: {
      versoes: [
        { nome: "Comum", preco: 200 },
        { nome: "Ultra Raro", preco: 500 },
        { nome: "Edição Limitada", preco: 800 }
      ]
    } 
  }
);

use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': '4K Ultra HD Action Camera' },
  { 
    $set: {
      versoes: [
        { nome: "Comum", preco: 200 }
      ]
    } 
  }
);

use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'The Book of Concealment (Dungeons & Dragons) A Game Screen and Journal in One' },
  { 
    $set: {
      versoes: [
        { nome: "Comum", preco: 200 },
        { nome: "Raro", preco: 500 }
      ]
    } 
  }
);

use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'Portable Bluetooth Speaker' },
  { 
    $set: {
      versoes: [
        { nome: "Comum", preco: 200 },
        { nome: "Raro", preco: 500 },
        { nome: "Edição Especial", preco: 800 },
        { nome: "Edição de Colecionador", preco: 1000 }
      ]
    } 
  }
);

use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'External SSD 1TB' },
  { 
    $set: {
      versoes: [
        { nome: "Comum", preco: 200 },
        { nome: "Edicição Ilimitada", preco: 500 }
      ]
    } 
  }
);

use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'Ergonomic Office Chair' },
  { 
    $set: {
      versoes: [
        { nome: "Comum", preco: 200 },
        { nome: "Ultra Raro+", preco: 500 }
      ]
    } 
  }
);

use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'Electric Toothbrush' },
  { 
    $set: {
      versoes: [
        { nome: "Comum", preco: 200 },
        { nome: "Raro", preco: 500 },
        { nome: "Edição Limitada", preco: 800 }
      ]
    } 
  }
)

// Mínimo de 5 clientes que já adquiriram o item.
use('EcommerceDB');
db.getCollection('produtos').updateOne(
  { 'nome_item': 'External SSD 1TB' },
  { 
    $push: { 'clientes_interessados': [
      'Maria Silva',
      'João Pereira',
      'Ana Costa',
      'Carlos Souza',
      'Fernanda Lima'
    ]} 
  }
);

use('EcommerceDB');
db.getCollection('produtos').find({ "nome_item": 'External SSD 1TB' });

// Uma fila de espera (ou lista de desejos) ativa.
use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'External SSD 1TB' },
  { 
    $set: {
      lista_desejos: [
        { usuario: "Daniel Rodrigues" },
      ]
    }
  }
);

use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'The Book of Concealment (Dungeons & Dragons) A Game Screen and Journal in One' },
  { $set: { lista_desejos: [ { usuario: "Daniel Rodrigues" } ] } }
);

db.getCollection('produtos').updateMany(
  { 'nome_item': 'Wireless Noise Cancelling Headphones' },
  { $set: { lista_desejos: [ { usuario: "Maria Silva" } ] } }
);

db.getCollection('produtos').updateMany(
  { 'nome_item': 'Mechanical Gaming Keyboard RGB' },
  { $set: { lista_desejos: [ { usuario: "João Pereira" } ] } }
);

db.getCollection('produtos').updateMany(
  { 'nome_item': 'Smart LED Light Bulb' },
  { $set: { lista_desejos: [ { usuario: "Ana Costa" } ] } }
);

db.getCollection('produtos').updateMany(
  { 'nome_item': '4K Ultra HD Action Camera' },
  { $set: { lista_desejos: [ { usuario: "Carlos Souza" } ] } }
);

db.getCollection('produtos').updateMany(
  { 'nome_item': 'Portable Bluetooth Speaker' },
  { $set: { lista_desejos: [ { usuario: "Fernanda Lima" } ] } }
);

db.getCollection('produtos').updateMany(
  { 'nome_item': 'Ergonomic Office Chair' },
  { $set: { lista_desejos: [ { usuario: "Bruno Alves" } ] } }
);

db.getCollection('produtos').updateMany(
  { 'nome_item': 'External SSD 1TB' },
  { $set: { lista_desejos: [ { usuario: "Daniel Rodrigues" } ] } }
);

db.getCollection('produtos').updateMany(
  { 'nome_item': 'CD do Jonnhy Silverhand (Cyberpunk 2077) - Edição de Colecionador' },
  { $set: { lista_desejos: [ { usuario: "Patrícia Gomes" } ] } }
);


// Uma seção de avaliações/comentários dos usuários.
use('EcommerceDB');
db.getCollection('produtos').updateMany(
  { 'nome_item': 'External SSD 1TB' },
  { 
    $set: {
      comentarios: [
        { comentario: "Produto Top!", usuario: "Ana Costa" }
      ]
    }
  }
);

//-----------------------------------------