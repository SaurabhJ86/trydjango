from rest_framework import serializers

from book.models import Book


class BookSerializers(serializers.ModelSerializer):
	user 			= serializers.StringRelatedField(many=False)
	author_new 		= serializers.StringRelatedField(many=False)
	genre 			= serializers.StringRelatedField(many=True)
	
	class Meta:
		model = Book
		fields = [
			"user",
			"author_new",
			"pages",
			"price",
			"ratings",
			"fictional",
			"book_type",
			"genre",
			"summary",
			"is_active",
		]