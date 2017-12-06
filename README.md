Setup a server able to run Selenium tests, via Python.

Control machine = the machine Ansible will run on
Client machine = the machine that Selenium will be setup on

NOTES: 
1. Tested with Client machines running Ubuntu 16.04.3. Other releases *should* work. Other distributions were **not** tested.
2. Some deprecation warnings (caused by upstream code) might be thrown. They can be ignored.

Control machine setup
---------------------

Ensure you have Ansible installed.

On Ubuntu, run:

`sudo easy_install pip`

`sudo pip install ansible`

Other OSs, check [http://docs.ansible.com/ansible/latest/intro_installation.html](http://docs.ansible.com/ansible/latest/intro_installation.html)

Confirm Ansible works ok by running:

`ansible --version`


Client machine setup
--------------------

Ensure there is a user on the client machine and you are able to SSH with it from the Control machine.


Setting up the client machine
-----------------------------

1. Add the IP(s) of the client machine(s) to the `hosts` file (in the root directory of this repo), under `[test_runners]`
2. Change the `client_user` in `vars/main.yml` to the username you created on the Client machine
3. Ensure all Ansible roles are available on the Control machine by running the following command on your Control machine, in the root of this repo:

`ansible-galaxy install -r requirements.yml`

3. Start the Client machine setup by running the following command on your Control machine, in the root of this repo:

`ansible-playbook provision.yml`