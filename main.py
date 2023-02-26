import openai
from aiogram import Bot, types, Dispatcher, executor

bot = Bot("6179571731:AAGLvplhbJdi1L5NGcewOM-O4Z2M5fOxjjU")
dp = Dispatcher(bot)

openai.api_key = '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'

@dp.message_handler(commands="start")
async def hello_message(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://www.rollingstone.com/wp-content/uploads/2018/06/rs-219361-SW_ep4_090___.jpg?resize=300")
    await message.answer(text=f"Привет! Я chat GPT, но теперь я научился использовать телеграмм для общения с пользователями!\n"
                              "Можешь писать мне на любом удобном для тебя языке. Чтобы начать общаться просто напиши своё сообщение мне в чат.")
    await message.delete()


@dp.message_handler()
async def message_sender(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" You:"]
    )

    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)