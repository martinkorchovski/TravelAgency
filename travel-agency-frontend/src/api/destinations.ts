const BASE_URL = 'http://127.0.0.1:8000'

export async function getDestinations() {
  const response = await fetch(`${BASE_URL}/api/destinations/`)
  const data = await response.json()
  return data.map((dest: any) => ({
    ...dest,
    image: dest.image ? `${BASE_URL}${dest.image}` : 'https://images.unsplash.com/photo-1506929562872-bb421503ef21?w=500'
  }))
}

export async function getHotelsByDestination(destinationId: number) {
  const response = await fetch(`${BASE_URL}/api/hotels/?destination=${destinationId}`)
  const data = await response.json()
  return data.map((hotel: any) => ({
    ...hotel,
    image: hotel.image ? hotel.image : 'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=500'
  }))
}

export async function getReviewsByHotel(hotelId: number) {
  const response = await fetch(`http://127.0.0.1:8000/api/reviews/?hotel=${hotelId}`)
  return await response.json()
}