from odoo import models, fields, api


class NonConformite(models.Model):
    _name = 'non.conformite'
    _description = 'Fiche Non-Conformité'

    code = fields.Char(string="Code", required=True, copy=False, readonly=True, default="New")
    description = fields.Text(string="Description")
    reclamation_id = fields.Many2one('reclamation', string="Réclamation liée")
    date_detection = fields.Date(string="Date de détection")
    designation_produit = fields.Char(
        string="Désignation du produit non conforme",
        required=True
    )
    produit_non_conforme_id = fields.Many2one(
        'product.product',
        string="Produit non conforme"
    )
    personnes_a_notifier_ids = fields.Many2many(
        'res.partner',
        string="Personnes à notifier"
    )
    type_non_conformite = fields.Selection(
        string="Type de non-conformité",
        selection=[
            ('qualite', 'Qualité'),
            ('securite', 'Sécurité'),
            ('reglementaire', 'Réglementaire'),
            ('autre', 'Autre')
        ],
        required=True
    )

    source_non_conformite = fields.Selection(
        string="Source de non-conformité",
        selection=[
            ('interne', 'Interne'),
            ('client', 'Client'),
            ('fournisseur', 'Fournisseur'),
            ('audit', 'Audit')
        ],
        required=True
    )

    niveau_gravite = fields.Selection(
        string="Niveau de gravité",
        selection=[
            ('mineure', 'Mineure'),
            ('majeure', 'Majeure'),
            ('critique', 'Critique')
        ],
        required=True
    )

    piece_jointe = fields.Binary(string="Pièce jointe")

    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('analyse', 'Analyse'),
        ('prise_en_charge', 'Prise en charge'),
        ('en_cours', 'En Cours'),
        ('cloturee', 'Clôturée'),
        ('annule', 'Annulée'),
    ], string='État', default='draft', readonly=True, tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            # Crée l'enregistrement normalement
            record = super(NonConformite, self).create(vals)
            # Attribue un code unique basé sur l'ID de l'enregistrement
            record.code = f"DOC-{record.id:02d}"
            return record
        return super(NonConformite, self).create(vals)

    def action_analyse(self):
        """Mettre l'état à 'Analyse'"""
        for record in self:
            record.state = 'analyse'

    def action_prise_en_charge(self):
        """Mettre l'état à 'Prise en charge'"""
        for record in self:
            record.state = 'prise_en_charge'

    def action_en_cours(self):
        """Mettre l'état à 'En cours'"""
        for record in self:
            record.state = 'en_cours'

    def action_cloturee(self):
        """Mettre l'état à 'Clôturée'"""
        for record in self:
            record.state = 'cloturee'

    def action_annule(self):
        """Mettre l'état à 'Annulée'"""
        for record in self:
            record.state = 'annule'

    def action_remettre_brouillon(self):
        """Remettre l'état à 'Brouillon'"""
        for record in self:
            record.state = 'draft'
