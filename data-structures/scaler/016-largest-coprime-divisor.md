
## Largest Coprime Divisor
- Ref: https://www.scaler.com/academy/mentee-dashboard/class/81691/homework/problems/358?navref=cl_tt_nv

## Question
![Question](http://ankit-portfolio.s3-ap-southeast-1.amazonaws.com/images/datastructures/scaler/016-largest-coprime-divisor-question.png)


### Approach
```py
class Solution:
    def cpFact(self, A, B):
        while True:
            out = self.gcd(A,B)
            if out == 1:
                return A
            A = A//out


    def gcd(self,A,B):
        if B==0:
            return A
        return self.gcd(B,A%B)


sol = Solution()
# print(sol.gcd(15,4))
# print(sol.gcd(5,4))

print(sol.cpFact(4,1))
print(sol.cpFact(30,12))
print(sol.cpFact(5,10))
```


Thank you for your time - Ankit

Hello Matthew,
Just wanted to drop in a thank you note for taking out time of your packed schedule and explaining me about the day to day job requirements.

Please allow me to share the meeting minutes.
- Thank you for:
  - Explaining me about OCI offerings: DRCC and OCI Alloy in sufficient detail.
  - Briefing me on the team size and it's component teams: pre-sales, Progam management team and Product Management team and how they all work together in tandem to make projects successful. 

- I got opportunity to explain about:
    - My career as an Engineer, Project Manager and my experiences with deployment of datacenter services to various cloud.
    - My Japanese skills.
    - Subtle differences in Japanese culture.
    - Strategy I use while deailing with completely unknown situations.
    - Enthusiasm for the role and how I can contribute about project successes.

I strongly hope that I left a positive mark during the interview.



Thank you for taking out time and briefing me about the role. It was great talking to you and I learnt 


Subject: Thank You for the TPM Opportunity Discussion

Hello Matthew,

Thank you for your time today. It was a pleasure to meet with you and learn more about the exciting work happening at your organization.

I am genuinely impressed by your team's commitment for expansion of OCI services in APAC region. Our discussion about expansion of OCI services, more specifically on OCI-DRCC and OCI-Alloy offerings  was particularly intriguing, and I am even more enthusiastic about the prospect of contributing to your team.

I believe that my prior experience, including my engineering role at Rakuten, where I played a pivotal role in migrating services to cloud environments, perfectly aligns with the demands of this position. Additionally, my recent project management experience, which involved Affiliate Marketing platform requirements breakdown,facilitating sprints and backlog refinement,diverse team and vendor management,handling project roadmaps and providing regular updates to  JP stakeholders on project progress and KPIs such as burndown chart, bugs ratio, teams velocities has equipped me with the skills necessary to effectively manage the delivery of OCI solutions to APAC customers. My AWS and Kubernetes cloud certifications knowledge along with my proficiency in both spoken and written Japanese will be a valuable asset in negotiating contracts and ensuring their successful completion. 

Nonetheless, I feel that this role will give me tremendous opportunity to work more closely with end customers.

Thank you again for considering me for this position. I am very interested in joining your team and would welcome the opportunity to provide any additional information or references you may need.

Please feel free to reach out to me at +65-98-777-601 or agarwal-ankit@live.in if you require any further information or clarification. I appreciate your time and consideration.

Once again, thank you for the opportunity, and I hope to hear from you soon.

Sincerely,
Ankit Agrawal