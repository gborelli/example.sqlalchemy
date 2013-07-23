example.sqlalchemy
==================

Esempio d'uso del traversing in Plone

Il pacchetto contiene una sola vista '@@messages' che elenca tutti gli elementi della tabella 'messages' così composta.

* message_id
* title
* year


dalla vista 'messages' è possibile filtrare gli elementi per anno cliccando sull'anno rappresentato nella vista o visualizzare il singolo elemento cliccando sul titolo.


La vista si occupa di filtrare gli elementi in base all'url a cui si accede in questa forma:
* <plone>/messages/<anno>
* <plone>/messages/<anno>/<message_id>


Ulteriore documentazione
------------------------

* Traversing in Plone - http://developer.plone.org/serving/traversing.html#custom-traversal
* connessione al db con sqlalchemy - https://pypi.python.org/pypi/z3c.saconfig
* Tutorial per l'uso del traversing - http://www.giorgioborelli.it/blog/integrazione-di-plone-con-database-sql
* Altro tutorial - http://www.giorgioborelli.it/blog/crud-form-e-sqlalchemy
