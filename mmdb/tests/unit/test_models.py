from django.test import TestCase

from mmdb.models import (
    Source,
    Media,
    Substances,
    Files,
    HarmonizedRaw,
    HarmonizedAggregate,
)


class TestModels(TestCase):
    def testSource(self):
        source = Source.objects.create()
        self.assertIsNotNone(source)
        self.assertIsNotNone(source.id)
        self.assertIsNotNone(source.processed)
        self.assertIsNotNone(source.harm_init)
        self.assertIsNotNone(source.harm_mapped)
        self.assertIsNotNone(source.loaded)
        self.assertFalse(source.processed)
        self.assertFalse(source.harm_init)
        self.assertFalse(source.harm_mapped)
        self.assertFalse(source.loaded)

    def testMedia(self):
        media = Media.objects.create()
        self.assertIsNotNone(media)
        self.assertIsNotNone(media.id)
        self.assertIsNone(media.source)

    def testSubstances(self):
        source = Source.objects.create()
        substances = Substances.objects.create(source=source)
        self.assertIsNotNone(substances)
        self.assertIsNotNone(substances.id)
        self.assertIsNotNone(substances.source)

    def testFiles(self):
        source = Source.objects.create()
        files = Files.objects.create(source=source)
        self.assertIsNotNone(files)
        self.assertIsNotNone(files.id)
        self.assertIsNotNone(files.source)
        self.assertIsNotNone(files.mapped)
        self.assertIsNotNone(files.harm_init)
        self.assertFalse(files.mapped)
        self.assertFalse(files.harm_init)
        self.assertIsNone(files.raw_init)

    def testHarmonizedRaw(self):
        source = Source.objects.create()
        files = Files.objects.create(source=source)
        media = Media.objects.create()
        harmonized = HarmonizedRaw.objects.create(
            files=files, source=source, media=media, record_id=1
        )
        self.assertIsNotNone(harmonized)
        self.assertIsNotNone(harmonized.id)
        self.assertIsNotNone(harmonized.files)
        self.assertIsNotNone(harmonized.source)
        self.assertIsNotNone(harmonized.media)
        self.assertIsNotNone(harmonized.record_id)
        self.assertIsNone(harmonized.detected)
        self.assertIsNone(harmonized.detect_conflict)

    def testHarmonizedAggregate(self):
        source = Source.objects.create()
        files = Files.objects.create(source=source)
        media = Media.objects.create()
        harmonized = HarmonizedAggregate.objects.create(
            files=files, source=source, media=media, record_id=1
        )
        self.assertIsNotNone(harmonized)
        self.assertIsNotNone(harmonized.id)
        self.assertIsNotNone(harmonized.files)
        self.assertIsNotNone(harmonized.source)
        self.assertIsNotNone(harmonized.media)
        self.assertIsNotNone(harmonized.record_id)
        self.assertIsNone(harmonized.detected)
        self.assertIsNone(harmonized.detect_conflict)
