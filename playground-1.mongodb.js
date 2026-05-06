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

// Select the database to use.
use('test');

db.getCollection('produtos').insertOne(
  { 'nome': 'bola', 'categoria': "esporte", 'quantidade': 2, 'preco': 10, 'estoque': 5 }
);

db.getCollection('produtos').find();

db.getCollection('produtos').find({"nome":"bola"});

db.getCollection('produtos').find({"estoque": {$gt:2}});

db.getCollection('produtos').updateOne(
  { 'nome': 'bola' },
  { $set: { 'estoque': 10 } }
);

db.getCollection('produtos').updateOne(
  { 'nome': 'bola' },
  { $set: { 'preco': 200 } }
)

db.getCollection('produtos').deleteOne({ 'nome': 'bola' });