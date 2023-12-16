from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.start import contact, start_keyboards
from keyboards.inline.course_kb import courses, registration
from loader import dp, bot
from states.user_registration import UserRegistration
from utils.db_api.user_reg import add_users_to_db, create_users_table

user_informations = {}


@dp.message_handler(text='📚 Kurslarimiz')
async def kurs_keyboard(message: types.Message):
    photo = 'https://marsit.uz/images/tild6362-6431-4430-b636-663563313631___3_.jpg'
    await message.answer_photo(photo=photo, caption='Kurslarimiz haqida ma\'lumot...',
                               reply_markup=courses)
    await UserRegistration.course.set()


@dp.callback_query_handler(state=UserRegistration.course)
async def starter_keyboard(call: types.CallbackQuery, state: FSMContext):
    kursni_nomi = call.data
    if kursni_nomi == 'starter':
        photo_s = 'https://inter-nation.uz/prices/tab-img-1.webp'
        await call.message.answer_photo(photo=photo_s, caption='Starter kursi 3 oy davom etadi...',
                                        reply_markup=registration)
        await state.update_data(course='Starter kursi')

    elif kursni_nomi == 'frontend':
        photo_f = 'https://marsit.uz/images/tild6563-3039-4132-b664-356163646536_____1.png'
        await call.message.answer_photo(photo=photo_f, caption='Frontend kursi 6 oy davom etadi...',
                                        reply_markup=registration)
        await state.update_data(course='Frontend kursi')

    elif kursni_nomi == 'backend':
        photo_b = 'https://marsit.uz/images/tild6563-3039-4132-b664-356163646536_____1.png'
        await call.message.answer_photo(photo=photo_b, caption='Backend kursi 9 oy davom etadi...',
                                        reply_markup=registration)
        await state.update_data(course='Backend kursi')

    elif kursni_nomi == 'grafik':
        photo_g = 'https://marsit.uz/images/tild6563-3039-4132-b664-356163646536_____1.png'
        await call.message.answer_photo(photo=photo_g, caption='Grafik dizayn kursi 6 oy davom etadi...',
                                        reply_markup=registration)
        await state.update_data(course='Grafik dizayn kursi')

    elif kursni_nomi == '3d':
        photo_3 = 'https://marsit.uz/images/tild6563-3039-4132-b664-356163646536_____1.png'
        await call.message.answer_photo(photo=photo_3, caption='3D dizayn kursi 6 oy davom etadi...',
                                        reply_markup=registration)
        await state.update_data(course='3D dizayn kursi')

    elif kursni_nomi == 'back_to_main':
        await call.message.answer('Menyuni tanlang:', reply_markup=start_keyboards)
        await state.finish()

    elif kursni_nomi == 'registration':
        await call.message.answer('Ismingizni kiriting')
        await UserRegistration.next()  # ism state ga solib qo'yadi

    elif kursni_nomi == 'back_to_course':
        photo = 'https://marsit.uz/images/tild6362-6431-4430-b636-663563313631___3_.jpg'
        await bot.send_photo(chat_id=call.message.chat.id, photo=photo, caption='Kurslarimiz haqida ma\'lumot...',
                             reply_markup=courses)
        await UserRegistration.course.set()


@dp.message_handler(state=UserRegistration.name)
async def get_name(message: types.Message, state: FSMContext):
    ism = message.text
    await state.update_data(name=ism)
    await message.answer('Telefon raqamingizni kiriting', reply_markup=contact)
    await UserRegistration.next()


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=UserRegistration.phone)
async def get_contact(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone=phone_number)
    data = await state.get_data()
    user_informations.update(data)  # user_informations ga o'zlashtiradi
    user_informations.update({'user_id': message.from_user.id})  # user_id ni ham ovolamiz
    await message.answer(f'Siz ro\'yxatdan o\'tdingiz!\nTez orada siz bilan bog\'lanamiz...\n\n'
                         f'Ma\'lumotlar:\nIsm: {data.get("name")}\nTelefon raqam: {data.get("phone")}\nKurs: {data.get("course")}',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    create_users_table()
    await add_users_to_db(user_informations)
    print(user_informations)
