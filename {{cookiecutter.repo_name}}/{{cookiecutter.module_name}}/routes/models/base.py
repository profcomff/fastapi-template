from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    def __repr__(self) -> str:
        attrs = []
        for k, v in self.__class__.schema().items():
            attrs.append(f"{k}={v}")
        return "{}({})".format(self.__class__.__name__, ", ".join(attrs))

    model_config = ConfigDict(from_attributes=True, extra="ignore")
