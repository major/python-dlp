# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for ListInfoTypes
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dlp


# [START dlp_generated_dlp_v2_DlpService_ListInfoTypes_async]
from google.cloud import dlp_v2


async def sample_list_info_types():
    # Create a client
    client = dlp_v2.DlpServiceAsyncClient()

    # Initialize request argument(s)
    request = dlp_v2.ListInfoTypesRequest(
    )

    # Make the request
    response = await client.list_info_types(request=request)

    # Handle response
    print(response)

# [END dlp_generated_dlp_v2_DlpService_ListInfoTypes_async]
