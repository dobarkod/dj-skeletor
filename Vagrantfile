Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible/playbook.yml"
        ansible.sudo = true
        ansible.verbose = 'vvvv'
        ansible.extra_vars = {
            app_user: "vagrant",
            app_home: "/vagrant"
        }
    end
end

Vagrant::Config.run do |config|
  config.vm.forward_port 80, 8000
end
