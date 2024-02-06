# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits
# Recode By : @SanzyDev

from asyncio import sleep

from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsKicked

from SanzyDev import CMD_HELP
from SanzyDev.sanzy import sanzy_cmd, eod, eor

from . import cmd

@sanzy_cmd(pattern="banall(?: |$)(.*)")
async def testing(SanzyDev):
    sanzy = await SanzyDev.get_chat()
    yins = await SanzyDev.client.get_me()
    admin = sanzy.admin_rights
    creator = sanzy.creator
    if not admin and not creator:
        await eod(SanzyDev, f"**Maaf {yins.first_name} Bukan Admin 👮**")
        return
    xnxx = await eor(SanzyDev, "Tidak Melakukan Apa-apa")
# Thank for Dark_Cobra
    sanzykontol = await SanzyDev.client.get_participants(SanzyDev.chat_id)
    for user in sanzykontol:
        if user.id == yins.id:
            pass
        try:
            xx = await SanzyDev.client(EditBannedRequest(SanzyDev.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await eod(xnxx, "**KESALAHAN : **`{}`".format(str(e)))
        await sleep(.5)
    await xnxx.edit("Tidak Ada yang Terjadi di sini🙃🙂")


@sanzy_cmd(pattern="unbanall(?: |$)(.*)")
async def _(sanzy):
    yins = await eor(sanzy, "`Sedang Mencari Daftar Blokir.`")
    p = 0
    (await sanzy.get_chat()).title
    async for i in sanzy.client.iter_participants(
        sanzy.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await sanzy.client.edit_permissions(sanzy.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await yins.edit(f"`Sukses Membebaskan {p} Tahanan...`")


CMD_HELP.update(
    {
        "yinsban": f"**Plugin : **`yinsban`\
        \n\n  »  **Perintah :** `{cmd}banall`\
        \n  »  **Kegunaan :** Banned Semua Member Dalam Satu Ketikan.\
        \n\n  »  **Perintah :** `{cmd}unbanall`\
        \n  »  **Kegunaan :** Membatalkan Banned Anggota Group.\
    "
    }
)
