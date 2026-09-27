import React from 'react'
import Card from './components/Card'

const App = () => {
  return (
    <div className='ml-5 flex gap-5 flex-wrap'>
      <Card title = 'checking title' description='this is description' img='https://images.unsplash.com/photo-1540553016722-983e48a2cd10?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=800&amp;q=80' />
      <Card title = 'checking title' description='this is description'  img='https://images.unsplash.com/photo-1788179612218-b98fc313b92d?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' />
      <Card title = 'checking title' description='this is description' img='https://images.unsplash.com/photo-1789693502198-fb38b839f168?q=80&w=1172&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' />
      <Card title = 'checking title' description='this is description' img='https://images.unsplash.com/photo-1789758385737-1125f82baa59?q=80&w=1400&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' />
      <Card title = 'checking title' description='this is description' img='https://images.unsplash.com/photo-1789665200787-370238007fc4?q=80&w=735&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' />
    </div>
  )
}

export default App
