# creat a file
file { 'school':
  path  => '/tmp/school',
  owner => 'www-data',
  group => 'www-data'
}
