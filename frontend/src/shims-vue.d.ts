declare module '*.vue' {
  import { DefineComponent } from 'vue';
  const component: DefineComponent<{}, {}, any>;
  export default component;
}

declare module '@/stores/*' {
  import { DefineStoreOptions } from 'pinia';
  const store: DefineStoreOptions<any, any, any, any>;
  export default store;
}

declare module '@/api/*' {
  const api: any;
  export default api;
}

declare module '@/layouts/*' {
  import { DefineComponent } from 'vue';
  const component: DefineComponent<{}, {}, any>;
  export default component;
}