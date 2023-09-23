from typing import Annotated

from fastapi import Depends

from base.utils import InterfaseContextManager, ContextManager


ContextManagerDepends = Annotated[InterfaseContextManager, Depends(ContextManager)]
