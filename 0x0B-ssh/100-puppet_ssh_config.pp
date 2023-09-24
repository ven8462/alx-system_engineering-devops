# puppet to log into a server without a password.

class { 'ssh::client':
  options => {
    'Host *' => {
      'PasswordAuthentication' => 'no',
      'IdentityFile' => '/home/codebind/.ssh/school',
    },
  },
}
