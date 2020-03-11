<template>
  <div id="app">
        <b-navbar toggleable="lg" type="dark" variant="info" :sticky="true">
            <b-navbar-brand to="/">Coronavirus COVID-19 Romania</b-navbar-brand>

<!--            <b-navbar-nav>-->
<!--                <b-nav-item to="turnout">-->
<!--                    Prezenta-->
<!--                </b-nav-item>-->
<!--                <b-nav-item to="turnout-list">-->
<!--                    Sectii-->
<!--                </b-nav-item>-->
<!--            </b-navbar-nav>-->
            <b-navbar-nav :small="true" class="ml-auto">
                <b-nav-text >Date furnizate de <a href="https://insp.gov.ro/">Institutul Național de Sănătate Publică</a>.
                </b-nav-text>
            </b-navbar-nav>

        </b-navbar>

        <b-container fluid>
            <b-row>
                <b-col cols="12 ">
                    <router-view></router-view>
                </b-col>
            </b-row>

        </b-container>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
