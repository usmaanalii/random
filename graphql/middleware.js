var express = require('express');
var graphqlHTTP = require('express-graphql');
var { buildSchema } = require('graphql');

// Construct a schema, using GraphQL schema language
var schema = buildSchema(`
    type Query {
        id: String
    }
`);

function loggingMiddleware(req, res, next) {
    console.log(`ip: ${req.ip}`);
    next();
}

var root = {
    ip: function (args, request) {
        return request.ip;
    }
};

var app = express();
app.use(loggingMiddleware);
app.use('/graphql', graphqlHTTP({
    schema: schema,
    rootValue: root,
    graphiql: true,
}));

app.listen(4000);
console.log('Running a GraphQL API server at localhost:4000/graphql');