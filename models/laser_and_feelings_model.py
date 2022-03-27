from datetime import datetime
from discord import Embed
from sqlalchemy import Integer, BigInteger, DateTime, String, Column, ForeignKey
from sqlalchemy.exc import SQLAlchemyError

from database import Base
from database.session_handler import select_all_from_where


class LAFModel(Base):
    """Model for Lasers And Feelings system"""
    __tablename__ = 'laser_and_feelings'
    character_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    character_name = Column(String(30), nullable=False, default='Nenhum nome definido')
    style = Column(String(15), default='Nenhum estilo definido')
    role = Column(String(15), default='Nenhum cargo definido')
    number = Column(Integer)
    goal = Column(String(50), default='Nenhum objetivo definido')
    created_at = Column(DateTime, default=datetime.utcnow())
    user_id = Column(BigInteger)

    @classmethod
    def get_characters(cls, user_id):
        try:
            return select_all_from_where(cls, user_id=user_id)
        except SQLAlchemyError as e:
            print(e)

    def show(self, character_name, style, role, goal, number, user_name, avatar_url):
        embed = Embed(color=0x7833bd)
        embed.set_author(name=user_name, icon_url=avatar_url)
        embed.add_field(name='Name', value=character_name)
        embed.add_field(name='Estilo', value=style, inline=True)
        embed.add_field(name='Cargo', value=role)
        embed.add_field(name='Objetivo', value=goal, inline=False)
        embed.add_field(name='Número', value=number, inline=False)
        embed.set_footer(text=':p')
        return embed