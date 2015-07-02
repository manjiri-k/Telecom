from openerp.osv import fields, osv

class telecom_project(osv.osv):
    _name="telecom.project"
    
    _columns={'name':fields.char(string='Project Name'),
              #'project_manager':fields.many2one('telecom.employee',string='Project Manager'),
              'circle':fields.many2one("telecom.circle",string="Circle"),
              'customer':fields.many2one("res.partner",string="Customer"),
              "start_date":fields.date(string="Start Date"),
              "end_date":fields.date(string="End Date"),
              'image':fields.binary("Bianry field"),
              'project_activities':fields.one2many('work.description','workdescription',string="Work Description"),
               'contact_no':fields.related('customer','phone',type="char",string="Contact No")
              }
class telecom_circle(osv.osv):
    _name='telecom.circle'
    _columns={'name':fields.char(string='Circle Name'),
              'project_name':fields.one2many('telecom.project','circle',string='Circle in Project')
              }
    
class work_description(osv.osv):
    _name="work.description"
    _columns={'name':fields.char(string='Activity Name'),
              'sub_activity':fields.one2many('project.activity',"activity",string='Project Activity'),
              'workdescription':fields.many2one("telecom.project")
              }
    
class project_activity(osv.osv):
    _name='project.activity'
    _columns={'name':fields.char(string='Activity Name'),
              'cost':fields.float(string="Cost"),
              #'time_to_complete':fields.datetime()
              'activity':fields.many2one('work.description'),
              }
class customers_customers(osv.osv):
    _name="telecom.customers"
    _columns={'name':fields.char(string='Customer Name'),
              'no_projects_undertaken':fields.integer(string='Total Project by customer'),
              'projects':fields.many2one("telecom.project",string="Projects"),
              
              }
