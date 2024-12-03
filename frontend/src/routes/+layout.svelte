<script lang="ts">
import "../app.css"
import { Navbar, NavBrand, NavHamburger, NavLi, NavUl, Dropdown, DropdownItem, DropdownDivider, BottomNav, BottomNavItem} from "flowbite-svelte"
import { page } from "$app/stores"
import { Menu, House, MapPinned, MessageSquareMore, Settings } from "lucide-svelte"
$: activeUrl = $page.url.pathname;
const activeClass = "text-primary bold underline stroke-primary";
const nonActiveClass = "text-text hover:text-primary";
</script>

<div class="min-h-screen flex flex-col overflow-hidden">
<Navbar class="px-2 sm:px-4 py-2.5 w-full z-30 top-0 start-0 border-b bg-background-foreground hidden md:block">
  <NavBrand href="/">
    <span class="self-center whitespace-nowrap text-xl text-primary dark:text-white font-primary font-normal">Parkpappa</span>
  </NavBrand>
  <NavHamburger />
  <NavUl {activeUrl} {activeClass} {nonActiveClass}>
    <NavLi href="/">Hem</NavLi>
    <NavLi href="/map">Karta</NavLi>
    <NavLi href="/reviews">Recensioner</NavLi>
    <NavLi class="cursor-pointer hidden md:block">
      More
      <Menu size=24 class="hidden md:inline"></Menu>
    </NavLi>
    <Dropdown class="w-40 z-20" containerClass="absolute">
      <DropdownItem href="/settings">Inställningar</DropdownItem>
      <DropdownItem href="/contact">Om oss</DropdownItem>
      <DropdownItem href="/about">Kontakta oss</DropdownItem>
      <DropdownDivider />
      <DropdownItem href="/">Sign out</DropdownItem>
    </Dropdown>
  </NavUl>
  
</Navbar>
  <main class="flex-grow flex flex-col">
    <slot></slot>
  </main>

  <div class="block md:hidden">
    <BottomNav classInner="grid-cols-4" {activeUrl} classActive="font-bold text-primary [&>*]:stroke-primary">
      <BottomNavItem btnName="Home" href="/">
        <House class="w-6 h-6 mb-1 text-gray-500 dark:text-gray-400 group-hover:text-primary-600 dark:group-hover:text-primary-500" />
      </BottomNavItem>
      <BottomNavItem btnName="Map" href="/map">
        <MapPinned class="w-6 h-6 mb-1 text-gray-500 dark:text-gray-400 group-hover:text-primary-600 dark:group-hover:text-primary-500" />
      </BottomNavItem>
      <BottomNavItem btnName="Review" href="/error">
        <MessageSquareMore class="w-6 h-6 mb-1 text-gray-500 dark:text-gray-400 group-hover:text-primary-600 dark:group-hover:text-primary-500" />
      </BottomNavItem>
      <BottomNavItem btnName="Settings" href="/error">
        <Settings class="w-6 h-6 mb-1 text-gray-500 dark:text-gray-400 group-hover:text-primary-600 dark:group-hover:text-primary-500" />
      </BottomNavItem>
    </BottomNav>
  </div>
</div>






