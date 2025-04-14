from odoo import models, fields


class action(models.Model):
    _name = 'action'
    _description = 'Gestion action'

    name = fields.Char(String="nom")
    # 1. Numéro séquentiel
    numero_sequentiel = fields.Char(
        string="Numéro Séquentiel",
        readonly=True,
        required=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('action.model') or '/'
    )

    # 2. Désignation
    designation = fields.Char(string="Désignation", required=True)

    # 3. Description
    description = fields.Text(string="Description")

    # 4. Type d'action
    type_action = fields.Selection(
        [
            ('type1', 'Type 1'),
            ('type2', 'Type 2'),
            ('type3', 'Type 3')
        ],
        string="Type d'Action",
        required=True
    )

    # 5. Source d'action
    source_action = fields.Selection(
        [
            ('source1', 'Source 1'),
            ('source2', 'Source 2'),
            ('source3', 'Source 3')
        ],
        string="Source d'Action",
        required=True
    )

    # 6. Cause de l'action
    cause_action = fields.Selection(
        [
            ('cause1', 'Cause 1'),
            ('cause2', 'Cause 2'),
            ('cause3', 'Cause 3')
        ],
        string="Cause de l'Action"
    )

    # 7. Gravité de l'action
    gravite_action = fields.Selection(
        [
            ('mineur', 'Mineur'),
            ('majeur', 'Majeur'),
            ('critique', 'Critique')
        ],
        string="Gravité de l'Action",
        required=True
    )

    # 8. Priorité de l'action
    priorite_action = fields.Selection(
        [
            ('basse', 'Basse'),
            ('moyenne', 'Moyenne'),
            ('haute', 'Haute'),
            ('urgente', 'Urgente')
        ],
        string="Priorité de l'Action",
        required=True
    )

    # 9. Responsable de validation de la demande d'action
    responsable_validation = fields.Many2one(
        'hr.employee',
        string="Responsable de Validation",
        required=True
    )

    # 10. Site
    site = fields.Selection(
        [
            ('site1', 'Site 1'),
            ('site2', 'Site 2'),
            ('site3', 'Site 3')
        ],
        string="Site Concerné"
    )
    numero_sequentiel = fields.Char(string='Numéro Séquentiel', readonly=True)
    responsable_realisation = fields.Many2one('hr.employee', string='Responsable de Réalisation')
    delai_realisation = fields.Datetime(string='Délai de Réalisation')
    responsable_suivi = fields.Many2one('hr.employee', string='Responsable de Suivi')
    delai_suivi = fields.Datetime(string='Délai de Suivi')
    gravite = fields.Selection([
        ('faible', 'Faible'),
        ('moyenne', 'Moyenne'),
        ('elevee', 'Élevée')
    ], string='Gravité')
    priorite = fields.Selection([
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute')
    ], string='Priorité')
    piece_jointe = fields.Binary(string='Pièce Jointe')
    taux_realisation = fields.Float(string='Taux de Réalisation')
    depenses = fields.Float(string='Dépenses (en dt)')
    commentaire = fields.Text(string='Commentaire')

    action_id = fields.Many2one('action', string='Action Principale')
    # Champs principaux de l'action
    numero_sequentiel = fields.Char(string="Numéro Séquentiel", readonly=True)
    designation = fields.Char(string="Désignation")
    description = fields.Text(string="Description")
    type_action = fields.Selection([
        ('prevention', 'Prévention'),
        ('correction', 'Correction'),
        ('amelioration', 'Amélioration'),
    ], string="Type d'Action")
    source_action = fields.Char(string="Source de l'Action")
    cause_action = fields.Text(string="Cause de l'Action")
    gravite_action = fields.Selection([
        ('faible', 'Faible'),
        ('moyenne', 'Moyenne'),
        ('elevee', 'Elevée'),
    ], string="Gravité de l'Action")
    priorite_action = fields.Selection([
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
    ], string="Priorité de l'Action")
    site = fields.Char(string="Site")
    responsable_validation = fields.Many2one('hr.employee', string="Responsable de Validation")

    # Champs pour les sous-actions
    responsable_realisation = fields.Many2one('hr.employee', string="Responsable de Réalisation")
    delai_realisation = fields.Datetime(string="Délai de Réalisation")
    responsable_suivi = fields.Many2one('hr.employee', string="Responsable de Suivi")
    delai_suivi = fields.Datetime(string="Délai de Suivi")
    gravite = fields.Selection([
        ('faible', 'Faible'),
        ('moyenne', 'Moyenne'),
        ('elevee', 'Elevée'),
    ], string="Gravité")
    priorite = fields.Selection([
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
    ], string="Priorité")
    piece_jointe = fields.Binary(string="Pièce Jointe")
    taux_realisation = fields.Float(string="Taux de Réalisation")
    depenses = fields.Float(string="Dépenses")
    commentaire = fields.Text(string="Commentaire")

    # Champs pour la clôture de l'action
    responsible_id = fields.Many2one(
        'hr.employee', string="Responsable de clôture",
        help="Employé en charge de la clôture de l'action."
    )
    closure_deadline = fields.Datetime(
        string="Délai de clôture",
        help="Date limite pour la clôture de l'action."
    )
    action_effectiveness = fields.Selection(
        [('inefficace', 'Inefficace'),
         ('partiellement_efficace', 'Partiellement efficace'),
         ('efficace', 'Efficace')],
        string="Efficacité de l'action",
        help="Niveau d'efficacité de l'action."
    )
    closure_attachment = fields.Binary(
        string="Pièce jointe (clôture)",
        help="Fichiers joints pour la clôture de l'action (optionnel)."
    )
    closure_comment = fields.Text(
        string="Commentaire (clôture)",
        help="Remarques finales sur la clôture."
    )

    # 28. État de la demande d'action
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('validated', 'Validée'),
        ('in_progress', 'En cours'),
        ('completed', 'Réalisée'),
        ('closed', 'Clôturée'),
    ], string="État de la demande", default='draft', required=True, track_visibility='onchange')

    # 29. Alerte pour responsables
    alert_responsible = fields.Boolean(string="Alerte activée", default=False)

    # 30. Traçabilité des modifications
    modification_history_ids = fields.Many2one(
        'hr.employee', string="Historique des modifications")
