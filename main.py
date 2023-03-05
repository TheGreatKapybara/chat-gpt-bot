import openai
from aiogram import Bot, types, Dispatcher, executor


bot = Bot("6179571731:AAGLvplhbJdi1L5NGcewOM-O4Z2M5fOxjjU")
dp = Dispatcher(bot)

openai.api_key = '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'

pin_counter = 0
@dp.message_handler(commands=["start", "help"])
async def hello_message(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=open("images/welcome_img.png", "rb"))
    to_pin = await message.answer(text=f"Привет! Я chat GPT, но теперь я научился использовать телеграмм для общения с пользователями!\n"
                              "Можешь писать мне на любом удобном для тебя языке. Чтобы начать общаться просто напиши своё сообщение мне в чат.")
    global pin_counter
    if pin_counter < 1:
        await bot.pin_chat_message(chat_id=message.from_user.id, message_id=to_pin.message_id)
        pin_counter += 1
    await message.delete()


@dp.message_handler()
async def message_sender(message: types.Message):
    bot_thinking_message = await message.answer(text="Я думаю🤔")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    await bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])
    await bot.delete_message(message_id=bot_thinking_message.message_id, chat_id=message.from_user.id)

executor.start_polling(dp, skip_updates=True)


