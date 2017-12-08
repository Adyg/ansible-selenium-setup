Setup a server able to run Selenium tests and notify via email&phone in case of failure.

Control machine = the machine Ansible will run on
Client machine = the machine that Selenium will be setup on


This was tested with Client machines running Ubuntu 16.04.3. Other releases *should* work. Other distributions were **not** tested.

Some deprecation warnings (caused by upstream code) might be thrown. They can be ignored.

One of the Ansible tasks ("Register systemd service status") will fail. Can be ignored.

What you will need
------------------
1. A [Sendgrid](https://sendgrid.com/) account and it's API credentials
2. A [Twilio](https://www.twilio.com/) account and it's API crendetials and phone number
3. A server that you are able to SSH to (the Client machine)


SETUP: Control machine setup
---------------------

Ensure you have Ansible installed.

On Ubuntu, run:

`sudo easy_install pip`

`sudo pip install ansible`

Other OSs, check [http://docs.ansible.com/ansible/latest/intro_installation.html](http://docs.ansible.com/ansible/latest/intro_installation.html)

Confirm Ansible works ok by running:

`ansible --version`

Once the Control machine is ready:

1. Add the IP(s) of the client machine(s) to the `hosts` file (in the root directory of this repo), under `[test_runners]`
2. Change the `client_user` in `vars/main.yml` to the username you created on the Client machine
3. Add the credentials for Sendgrid and Twilio to `vars/main.yml`
4. Ensure all Ansible roles are available on the Control machine by running the following command on your Control machine, in the root of this repo:

`ansible-galaxy install -r requirements.yml`

5. Start the Client machine setup by running the following command on your Control machine, in the root of this repo:

`ansible-playbook provision.yml`