import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Box, Button, Input, Stack, FormControl, FormLabel, Heading, Alert, AlertIcon, Image, Center, Divider } from '@chakra-ui/react';
import fondoLogin from '../assets/login-barberia.jpeg';
import logo from '../assets/logo.png';

function Login({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    if (username === 'matiuveas' && password === 'admin') {
      const userData = {
        name: 'Matthieu Veas',
        comuna: 'Valdivia'
      };
      onLogin(userData);
      navigate('/main-menu');
    } else {
      setError('Usuario o contraseña incorrectos');
    }
  };

  return (
    <Box
      position="relative"
      width="100vw"
      height="100vh"
      bgImage={`url(${fondoLogin})`}
      bgPosition="center"
      bgRepeat="no-repeat"
      bgSize="cover"
      _before={{
        content: '""',
        position: "absolute",
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        bg: "rgba(0, 0, 0, 0.5)",
        filter: "blur(10px)",
        zIndex: 1,
      }}
    >
      <Center position="relative" zIndex={2} height="100%">
        <Box
          maxW="md"
          width="100%"
          p={6}
          borderRadius="md"
          bg="white"
          boxShadow="md"
          textAlign="center"
        >
          <Image src={logo} boxSize="auto" objectFit="cover" mx="auto" />
          <Divider borderColor="black" my={4} />
          <Heading mb={6} marginTop={'5'} fontSize={32}>Iniciar Sesión</Heading>
          <Divider borderColor="black" my={4} />
          {error && (
            <Alert status="error" mb={4}>
              <AlertIcon />
              {error}
            </Alert>
          )}
          <Stack spacing={4}>
            <FormControl>
              <FormLabel>Usuario</FormLabel>
              <Input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </FormControl>
            <FormControl>
              <FormLabel>Contraseña</FormLabel>
              <Input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </FormControl>
            <Button colorScheme="blue" onClick={handleLogin}>
              Iniciar Sesión
            </Button>
          </Stack>
        </Box>
      </Center>
    </Box>
  );
}

export default Login;
