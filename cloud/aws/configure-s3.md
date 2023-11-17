
```bash
## Get VPC ID
aws ec2 describe-vpcs --filters "Name=cidr-block,Values=10.0.0.0/16" --query 'Vpcs[].[VpcId]'

## Get associated route tables
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=VpcId"

## Create VPC endpoint
aws ec2 create-vpc-endpoint --vpc-id VpcId --vpc-endpoint-type Gateway --service-name com.amazonaws.eu-west-1.s3 --route-table-ids routeTableId

## Create S3 bucket
aws s3api create-bucket --bucket ankit-portfolio --region ap-southeast-1 --create-bucket-configuration LocationConstraint=ap-southeast-1

# http://ankit-portfolio.s3.amazonaws.com

## Test bucket
touch testfilelocallyopen.txt
aws s3 cp testfilelocallyopen.txt s3://ankit-portfolio/testfilelocallyopen.txt
aws s3 ls s3://ankit-portfolio/

## Check IP address
curl https://checkip.amazonaws.com

```

## Attach Policy for restricted IP address access

```bash
aws s3api put-bucket-policy --bucket ankit-portfolio --policy file://policy.json
```

```json
{
  "Id": "SourceIP",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SourceIP",
      "Action": "s3:GetObject",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::ankit-portfolio/*",
      "Condition": {
        "NotIpAddress": {
          "aws:SourceIp": [
            "*/32"
          ]
        }
      },
      "Principal": "*"
    }


  ]
}

{
  "Id": "SourceIP",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SourceIP",
      "Action": "s3:GetObject",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::ankit-portfolio/*",
      "Principal": "*"
    }


  ]
}

```

## Create user for AWS s3 bastion access

```bash
# Create user
aws iam create-user \
    --user-name ec2 \
    --permissions-boundary arn:aws:iam::aws:policy/AmazonS3FullAccess

# Create access key
aws iam create-access-key \
    --user-name ec2

# Configure aws in bastion host using secret key ID and secret key
aws configure
AWS Access Key ID [None]: <KEY_ID>
AWS Secret Access Key [None]: <KEY>
Default region name [None]: ap-southeast-1
Default output format [None]:

# Delete user
aws iam delete-access-key \
    --access-key-id <KEY>  --user-name ec2
aws iam delete-user --user-name ec2
```


### Attach user to group

```bash
aws iam list-groups

aws iam add-user-to-group \
    --user-name ec2 \
    --group-name training-group
```