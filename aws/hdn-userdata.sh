#!/bin/bash
sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
mkdir /home/ec2-user/hdn
aws s3 sync s3://gmod-hdn /home/ec2-user/hdn

IPV4=$(curl 169.254.169.254/latest/meta-data/public-ipv4)
aws route53 change-resource-record-sets --hosted-zone-id Z3OPAVCB13L0BG --change-batch "{
   \"Changes\":[
      {
         \"Action\":\"UPSERT\",
         \"ResourceRecordSet\":{
            \"Name\":\"hdn.itisamystery.com\",
            \"ResourceRecords\":[
               {
                  \"Value\":\"$IPV4\"
               }
            ],
            \"Type\":\"A\",
            \"TTL\":300
         }
      }
   ]
}"

docker run -idt -e "GLST=04285C34D64799830F63FC216DAF94B4" -e "WORKSHOP=2091506439" -e "WORKSHOPDL=2091506439" -e "WORKSHOPCOLLECTIONID=2091506439" -e "GAMEMODE=thehidden" -e "MAP=hdn_executive" -p 27015:27015/tcp -p 27015:27015/udp -v /home/ec2-user/hdn:/opt/steam hackebein/garrysmod
