from dataclasses import dataclass


@dataclass
class Source:
    name: str
    url: str


sources: list[Source] = [
    Source(name="👾 Space", url="https://www.youtube.com/watch?v=tNkZsRW7h2c"),
    Source(name="☕ Spain Cafe", url="https://www.youtube.com/watch?v=Uc9OfTZeezY"),
    Source(name="🚋 Swiss train", url="https://www.youtube.com/watch?v=3bKOl7HWo14"),
    Source(name="🦇 Batman", url="https://www.youtube.com/watch?v=mPhl23eo69g"),
    Source(name="🔄 Don't know", url="https://www.youtube.com/watch?v=ZgIApioi-jE"),
    Source(name="🐭 Disney Piano", url="https://www.youtube.com/watch?v=jIp4J62aRvY"),
    Source(name="🌩️ Storm", url="https://www.youtube.com/watch?v=ZgIApioi-jE"),
    Source(name=" ☺️ Bossa Nova", url="https://www.youtube.com/watch?v=nSruEZl0Gro"),
    Source(name="🎷 Jazz", url="https://www.youtube.com/watch?v=xl0NMRAnqbA"),
    Source(name="🎞️ BSO 1", url="https://www.youtube.com/watch?v=BbbWJIvb94c"),
    Source(name="🎞️ BSO 2", url="https://www.youtube.com/watch?v=8H29XVCOt8M"),
    Source(name=" 🪐 Interstellar", url="https://www.youtube.com/watch?v=YF1eYbfbH5k"),
    Source(name="🔫 Blade Runner", url="https://www.youtube.com/watch?v=RrkrdYm3HPQ"),
    Source(
        name="🐱 Anime Jazz",
        url="https://www.youtube.com/watch?v=BIZz4A39rT4&t=3569s",
    ),
    Source(name="🏰 Baldurs Gate 3", url="https://www.youtube.com/watch?v=BXluPbtRLqE"),
    Source(name="💍 LOTR", url="https://www.youtube.com/watch?v=K69tbUo3vGs"),
    Source(name="🐵 Monkey Island", url="https://www.youtube.com/watch?v=_fj5pIpjS14"),
    Source(name="💿 Hans Zimmer", url="https://www.youtube.com/watch?v=-zi5nENK1po"),
    Source(name="🏜️ Dune", url="https://www.youtube.com/watch?v=uTmBeR32GRA"),
    Source(name="⚔️ Zelda", url="https://www.youtube.com/watch?v=MXDF0wVcWfA&t=6627s"),
    Source(name="🐔 Final Fantasy", url="https://www.youtube.com/watch?v=DiYTaQ-Mgck"),
    Source(name="⛪ Vangelis", url="https://www.youtube.com/watch?v=4C2w5uMTvRY"),
]
