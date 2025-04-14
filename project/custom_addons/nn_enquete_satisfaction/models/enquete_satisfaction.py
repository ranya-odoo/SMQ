from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class EnqueteSatisfaction(models.Model):
    _name = 'enquete.satisfaction'
    _description = 'Enquête de Satisfaction Client'
    _order = 'date_debut desc'

    reference = fields.Char(string="Référence", required=True, copy=False, readonly=True, default="New")
    name = fields.Char(string="Référence de l'enquête", required=True, copy=False, readonly=True, default='New')
    date_debut = fields.Date(string="Date de début", default=fields.Date.context_today)
    date_fin = fields.Date(string="Date de fin")
    client_ids = fields.Many2many('res.partner', string="Clients concernés")

    type_questionnaire = fields.Selection([
        ('court', 'Court'),
        ('detaille', 'Détaillé'),
        ('custom', 'Personnalisé')
    ], string="Type de questionnaire", required=True)

    # Méthode d'envoi des emails
    def action_send_emails(self):
        for record in self:
            if not record.client_ids:
                raise UserError("Veuillez ajouter au moins un client avant d'envoyer l'enquête.")

            # Envoi des emails
            for client in record.client_ids:
                if client.email:
                    subject = f"Enquête de Satisfaction: {record.reference}"
                    body_html = """
                            <p>Bonjour {name},</p>
                            <p>Nous vous invitons à répondre à notre enquête de satisfaction concernant {reference}.</p>
                            <p>Cordialement,</p>
                        """.format(name=client.name, reference=record.reference)

                    # Création et envoi de l'email
                    mail_values = {
                        'email_to': client.email,
                        'subject': subject,
                        'body_html': body_html,
                        'email_from': self.env.user.email or 'noreply@exemple.com',
                    }
                    mail = self.env['mail.mail'].create(mail_values)
                    mail.send()

    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            record = super(EnqueteSatisfaction, self).create(vals)
            record.reference = f"DOC-{record.id:02d}"
            return record
        return super(EnqueteSatisfaction, self).create(vals)