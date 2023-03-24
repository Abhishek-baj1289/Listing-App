import ItemList from './ItemList'
import React from 'react'
// import SearchBar from './Search'

const Content = ({ items, handleCheck, handleDelete }) => {
  return (
    <main>
      {/* <SearchBar /> */}
      {items.length ? (
        <ItemList
          items={items}
          handleCheck={handleCheck}
          handleDelete={handleDelete} 
          />

      ) : (
        <p style={{ marginTop: '2rem' }}>Your list is empty</p>
      )}
    </main>
  )
}

export default Content

/*
Twinkle twinke little star
how i wonder what you are 
up above the world so high 
lika a diamond in the sky

when the blazing sun is gone
when the nothing shines upon 
then you show you little light 
twinkle twinkle all the night

then the traveller in the dark
will thank you for your little spark
for he could not see which way to go
if you did not twinkle so

in the dark blue sky you keep
often through my curtains peep
for you never shut your eye 
till the sun is in the sky

as your bright and tiny spark
light the traveller in the dark
though i not know what you are
twinke twinkle little star
*/