const BASE_URL = 'http://127.0.0.1:8000'

export async function getDestinations() {
  const response = await fetch(`${BASE_URL}/api/destinations/`)
  const data = await response.json()
  return data.map((dest: any) => ({
    ...dest,
    image: dest.image ? `${BASE_URL}${dest.image}` : 'https://images.unsplash.com/photo-1506929562872-bb421503ef21?w=500'
  }))
}