Setup a server able to run Selenium tests and notify via email&phone in case of failure.

Definitions
----------------

Control machine = the machine Ansible will run on (your local dev machine)

Client machine = the machine that Selenium will be setup on


Notes
-----

This was tested with Client machines running Ubuntu 16.04.3. Other releases *should* work. Other distributions were **not** tested.

Some deprecation warnings (caused by upstream code) might be thrown. They can be ignored.

One of the Ansible tasks ("Register systemd service status") will fail. Can be ignored.


What you will need
------------------
1. A [Sendgrid](https://sendgrid.com/) account and it's API credentials (Full Access)
2. A [Twilio](https://www.twilio.com/) account and it's API crendetials and phone number
3. A fresh server that you are able to SSH to (the Client machine)


SETUP: Control machine setup
---------------------

1. Ensure you have Ansible installed.

  a. On Ubuntu, run:

  `sudo easy_install pip`

  `sudo pip install ansible`

  Other OSs, check [http://docs.ansible.com/ansible/latest/intro_installation.html](http://docs.ansible.com/ansible/latest/intro_installation.html)

  b. Confirm Ansible works ok by running:

  `ansible --version`

  c. Ensure all Ansible roles are available on the Control machine by running the following command on your Control machine, in the root of this repo:

  `ansible-galaxy install -r requirements.yml`


2. Once the Control machine is ready:

  a. Add the IP(s) of the client machine(s) to the `hosts` file (in the root directory of this repo), under `[test_runners]`. Each IP on a new line.

  b. Change the `client_user` in `vars/main.yml` to the username you created on the Client machine

  c. Add the credentials for Sendgrid and Twilio (get them from [https://www.twilio.com/console/sms/dashboard](https://www.twilio.com/console/sms/dashboard)) to `vars/main.yml`

  d. Add the emails that will be notified to `send_email_notifications_to` in `vars/main.yml`, comma separated
  
  e. Add the phone numbers that will be notified to `send_sms_notifications_to` in `vars/main.yml`, comma separated


SETUP: Client machine setup
---------------------------

1. Start the Client machine setup by running the following command on your Control machine, in the root of this repo:

`ansible-playbook provision.yml`

