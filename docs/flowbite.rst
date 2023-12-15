- not too sure about json.dumps parameters
  transitionParams=json.dumps({'duration': 300}),

  
- spacing between accordion is an issue; talk to flowbite folks.

- what is the deal with Alert class="!items-start". Is !items-start in your library.

 Avatar
 .......
<Avatar src="/images/profile-picture-3.webp" dot={{ color: 'red' }} />
<Avatar src="/images/profile-picture-3.webp" dot={{ placement: 'top-right', color: 'red' }} rounded />
<Avatar src="/images/profile-picture-5.webp" dot={{ placement: 'bottom-right', color: 'green' }} />
<Avatar src="/images/profile-picture-5.webp" dot={{ placement: 'bottom-right' }} rounded />

Drop Down
``````````

<script>
  import { Avatar, Dropdown, DropdownHeader, DropdownItem, DropdownDivider } from 'flowbite-svelte';
</script>

<Avatar id="user-drop" src="/images/profile-picture-3.webp" class="cursor-pointer" dot={{ color: 'green' }} />
<Dropdown triggeredBy="#user-drop">
  <DropdownHeader>
    <span class="block text-sm">Bonnie Green</span>
    <span class="block truncate text-sm font-medium">name@flowbite.com</span>
  </DropdownHeader>
  <DropdownItem>Dashboard</DropdownItem>
  <DropdownItem>Settings</DropdownItem>
  <DropdownItem>Earnings</DropdownItem>
  <DropdownDivider />
  <DropdownItem>Sign out</DropdownItem>
</Dropdown>

Sizes
``````
<div class=" flex flex-wrap justify-center space-x-4 rtl:space-x-reverse">
  <Avatar src="/images/profile-picture-3.webp" rounded size="xs" />
  <Avatar src="/images/profile-picture-3.webp" rounded size="sm" />
  <Avatar src="/images/profile-picture-3.webp" rounded size="md" />
  <Avatar src="/images/profile-picture-3.webp" rounded size="lg" />
  <Avatar src="/images/profile-picture-3.webp" rounded size="xl" />
</div>



Banner
.......

Its horribly supported -- not even not working


