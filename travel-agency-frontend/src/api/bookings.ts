const BASE_URL = 'http://127.0.0.1:8000'

export async function getMyBookings(token: string) {
  const response = await fetch(`${BASE_URL}/api/bookings/my/`, {
    method: 'GET',
    headers: {
      Authorization: `Bearer ${token}`
    }
  })

  if (!response.ok) {
    throw new Error('Не може да се вчитаат резервациите')
  }

  return await response.json()
}
export async function cancelBooking(id: number, token: string) {
  const response = await fetch(
    `${BASE_URL}/api/bookings/${id}/status/`,
    {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        status: 'cancelled'
      })
    }
  )

  if (!response.ok) {
    throw new Error('Не може да се откаже резервацијата')
  }

  return await response.json()
}