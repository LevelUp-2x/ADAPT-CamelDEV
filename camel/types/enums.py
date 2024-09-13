# (Previous content remains unchanged)

class ModelType(Enum):
    # (Existing model types remain unchanged)

    # Add GitHub model types
    GITHUB_COPILOT = "github-copilot"
    GITHUB_CODEX = "github-codex"

    # Add Gemini model types
    GEMINI_PRO = "gemini-pro"
    GEMINI_PRO_VISION = "gemini-pro-vision"

    # (Rest of the ModelType class remains unchanged)

    @property
    def is_github(self) -> bool:
        r"""Returns whether this type of models is a GitHub model."""
        return self in {
            ModelType.GITHUB_COPILOT,
            ModelType.GITHUB_CODEX,
        }

    @property
    def is_gemini(self) -> bool:
        r"""Returns whether this type of models is a Gemini model."""
        return self in {
            ModelType.GEMINI_PRO,
            ModelType.GEMINI_PRO_VISION,
        }

    # (Rest of the ModelType class methods remain unchanged)


class ModelPlatformType(Enum):
    # (Existing platform types remain unchanged)
    GITHUB = "github"
    GEMINI = "gemini"

    # (Rest of the ModelPlatformType class remains unchanged)

    @property
    def is_github(self) -> bool:
        r"""Returns whether this platform is GitHub."""
        return self is ModelPlatformType.GITHUB

    @property
    def is_gemini(self) -> bool:
        r"""Returns whether this platform is Gemini."""
        return self is ModelPlatformType.GEMINI

    # (Rest of the ModelPlatformType class methods remain unchanged)

# (Rest of the file remains unchanged)
