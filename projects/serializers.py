from rest_framework import serializers
from .models import Project, Contributor, Comment, Issue


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'type',
            'author',
            'created_time']
        extra_kwargs = {
            'author': {'read_only': True}
        }


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            'id',
            'user',
            'project',
            'role']


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            'id',
            'title',
            'description',
            'tag',
            'priority',
            'status',
            'project',
            'author',
            'assignee',
            'created_time'
        ]
        extra_kwargs = {
            'author': {'read_only': True},
            'created_time': {'read_only': True},
        }

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'description',
            'author',
            'issue',
            'created_time'
        ]
        extra_kwargs = {
            'author': {'read_only': True},
            'created_time': {'read_only': True},
        }
