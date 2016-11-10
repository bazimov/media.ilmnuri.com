# media.ilmnuri.com

## ilmnuri.net webapp & android/iOS app backend server

## This app has api and website of ilmnuri apps. 

### App has an ansible playbook, that automatically configures the vm.

Run the playbook locally in the vm.

```ansible-playbook -i "localhost," -c local playbooks/ilmnuri-playbook.yml```

Run the playbook remotely, you need ilmnuri host in your ansible hosts file.

```ansible-playbook playbooks/ilmnuri-playbook.yml -l ilmnuri```

Run teh playbook from remote machine.
 1. First have inventory called ilmnuri in your /etc/ansible/hosts file

```ansible-playbook playbooks/ilmnuri-playbook.yml```
