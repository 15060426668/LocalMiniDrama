import request from '@/api/request';

export function listSkills() {
  return request.get('/skills');
}

export function getSkillInfo(name) {
  return request.get(`/skills/${name}`);
}

export function getSkillContent(name) {
  return request.get(`/skills/${name}/content`);
}