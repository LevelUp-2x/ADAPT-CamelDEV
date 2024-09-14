from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..config.database import Base

# Association table for many-to-many relationship between Documents and Entities
document_entity = Table('document_entity', Base.metadata,
    Column('document_id', Integer, ForeignKey('documents.id')),
    Column('entity_id', Integer, ForeignKey('entities.id'))
)

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    entities = relationship("Entity", secondary=document_entity, back_populates="documents")
    relationships = relationship("Relationship", back_populates="document")

class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    entity_type = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    documents = relationship("Document", secondary=document_entity, back_populates="entities")
    relationships_from = relationship("Relationship", foreign_keys="[Relationship.entity_from_id]", back_populates="entity_from")
    relationships_to = relationship("Relationship", foreign_keys="[Relationship.entity_to_id]", back_populates="entity_to")

class Relationship(Base):
    __tablename__ = "relationships"

    id = Column(Integer, primary_key=True, index=True)
    relationship_type = Column(String)
    entity_from_id = Column(Integer, ForeignKey('entities.id'))
    entity_to_id = Column(Integer, ForeignKey('entities.id'))
    document_id = Column(Integer, ForeignKey('documents.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    entity_from = relationship("Entity", foreign_keys=[entity_from_id], back_populates="relationships_from")
    entity_to = relationship("Entity", foreign_keys=[entity_to_id], back_populates="relationships_to")
    document = relationship("Document", back_populates="relationships")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SystemConfig(Base):
    __tablename__ = "system_configurations"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True)
    value = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())