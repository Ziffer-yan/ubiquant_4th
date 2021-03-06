# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import question_pb2 as question__pb2


class QuestionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.get_question = channel.unary_unary(
        '/Question/get_question',
        request_serializer=question__pb2.QuestionRequest.SerializeToString,
        response_deserializer=question__pb2.QuestionResponse.FromString,
        )


class QuestionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def get_question(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_QuestionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'get_question': grpc.unary_unary_rpc_method_handler(
          servicer.get_question,
          request_deserializer=question__pb2.QuestionRequest.FromString,
          response_serializer=question__pb2.QuestionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Question', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
