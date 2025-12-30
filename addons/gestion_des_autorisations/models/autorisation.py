from odoo import models, fields

class Autorisation(models.Model):
    _name = "gestion.autorisation"
    _description = "Autorisation d'accès"

    name = fields.Char(string="Nom de l'autorisation", required=True)
    utilisateur = fields.Many2one('res.users', string="Utilisateur")
    module = fields.Char(string="Module")
    niveau = fields.Selection([
        ('lecture', 'Lecture'),
        ('ecriture', 'Écriture'),
        ('admin', 'Administrateur')
    ], string="Niveau d'accès", default="lecture")
    date_creation = fields.Datetime(string="Date de création", default=fields.Datetime.now)
