class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            name, domain = email.split('@')
            name = name.replace('.', '')
            
            if '+' in name:
                name = name[:name.index('+')]
                
            email_set.add(name + '@' + domain)
        
        return len(email_set)
