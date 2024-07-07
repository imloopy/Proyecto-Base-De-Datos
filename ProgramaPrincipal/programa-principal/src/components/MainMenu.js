import React from 'react';
import { Box, Heading, Grid, Button, Flex, Text } from '@chakra-ui/react';

function MainMenu({ userName, sedeComuna }) {
  return (
    <Box maxW="1200px" mx="auto" mt={10} p={4}>
      <Flex justify="space-between" mb={6}>
        <Text fontSize="xl" fontWeight="bold">Bienvenido {userName}!</Text>
        <Text fontSize="xl" fontWeight="bold">Sede {sedeComuna}</Text>
      </Flex>
      <Heading mb={6} textAlign="center">Menú Principal</Heading>
      <Grid templateColumns="repeat(2, 1fr)" gap={6}>
        <Button colorScheme="blue" onClick={() => { /* Navegar a la página correspondiente */ }}>Página 1</Button>
        <Button colorScheme="blue" onClick={() => { /* Navegar a la página correspondiente */ }}>Página 2</Button>
        <Button colorScheme="blue" onClick={() => { /* Navegar a la página correspondiente */ }}>Página 3</Button>
        <Button colorScheme="blue" onClick={() => { /* Navegar a la página correspondiente */ }}>Página 4</Button>
      </Grid>
    </Box>
  );
}

export default MainMenu;
