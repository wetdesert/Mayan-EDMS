from __future__ import unicode_literals

from django.conf.urls import url

from .api_views import (
    APIDocumentMetadataListView, APIDocumentMetadataView,
    APIDocumentTypeMetadataTypeListView, APIDocumentTypeMetadataTypeView,
    APIMetadataTypeListView, APIMetadataTypeView
)
from .views import (
    DocumentMetadataAddView, DocumentMetadataEditView,
    DocumentMetadataListView, DocumentMetadataRemoveView,
    MetadataTypeCreateView, MetadataTypeDeleteView, MetadataTypeEditView,
    MetadataTypeListView, SetupDocumentTypeMetadataTypes,
    SetupMetadataTypesDocumentTypes
)

urlpatterns = [
    url(
        r'^documents/(?P<pk>\d+)/edit/$', DocumentMetadataEditView.as_view(),
        name='document_metadata_edit'
    ),
    url(
        r'^documents/multiple/edit/$', DocumentMetadataEditView.as_view(),
        name='document_multiple_metadata_edit'
    ),
    url(
        r'^documents/(?P<pk>\d+)/view/$', DocumentMetadataListView.as_view(),
        name='document_metadata_view'
    ),
    url(
        r'^documents/(?P<pk>\d+)/add/$', DocumentMetadataAddView.as_view(),
        name='document_metadata_add'
    ),
    url(
        r'^documents/multiple/add/$', DocumentMetadataAddView.as_view(),
        name='document_multiple_metadata_add'
    ),
    url(
        r'^documents/(?P<pk>\d+)/remove/$', DocumentMetadataRemoveView.as_view(),
        name='document_metadata_remove'
    ),
    url(
        r'^documents/multiple/remove/$', DocumentMetadataRemoveView.as_view(),
        name='document_multiple_metadata_remove'
    ),

    url(
        r'^types/list/$', MetadataTypeListView.as_view(),
        name='metadata_type_list'
    ),
    url(
        r'^types/create/$', MetadataTypeCreateView.as_view(),
        name='metadata_type_create'
    ),
    url(
        r'^types/(?P<pk>\d+)/edit/$', MetadataTypeEditView.as_view(),
        name='metadata_type_edit'
    ),
    url(
        r'^types/(?P<pk>\d+)/delete/$',
        MetadataTypeDeleteView.as_view(), name='metadata_type_delete'
    ),
    url(
        r'^document_types/(?P<pk>\d+)/metadata_types/$',
        SetupDocumentTypeMetadataTypes.as_view(),
        name='document_type_metadata_types'
    ),
    url(
        r'^metadata_types/(?P<pk>\d+)/document_types/$',
        SetupMetadataTypesDocumentTypes.as_view(),
        name='metadata_type_document_types'
    ),
]

api_urls = [
    url(
        r'^metadata_types/$', APIMetadataTypeListView.as_view(),
        name='metadatatype-list'
    ),
    url(
        r'^metadata_types/(?P<metadata_type_pk>\d+)/$',
        APIMetadataTypeView.as_view(), name='metadatatype-detail'
    ),
    url(
        r'^document_types/(?P<document_type_pk>\d+)/metadata_types/$',
        APIDocumentTypeMetadataTypeListView.as_view(),
        name='documenttypemetadatatype-list'
    ),
    url(
        r'^document_types/(?P<document_type_pk>\d+)/metadata_types/(?P<metadata_type_pk>\d+)/$',
        APIDocumentTypeMetadataTypeView.as_view(),
        name='documenttypemetadatatype-detail'
    ),
    url(
        r'^documents/(?P<document_pk>\d+)/metadata/$',
        APIDocumentMetadataListView.as_view(), name='documentmetadata-list'
    ),
    url(
        r'^documents/(?P<document_pk>\d+)/metadata/(?P<metadata_pk>\d+)/$',
        APIDocumentMetadataView.as_view(), name='documentmetadata-detail'
    ),
]
