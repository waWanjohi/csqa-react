import { Component } from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
const { Header, Footer, Sider, Content } = Layout;

// Get the year to change dynamically
const getYear = () => {
    let today = new Date();
    let year = today.getFullYear();
    return year;
}

class BaseLayout extends Component {

    render() {
        return (
            <Layout>
                <Header className="header site-layout-background">
                    <div className="logo" />
                    <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
                        <Menu.Item key="1">nav 1</Menu.Item>
                        <Menu.Item key="2">nav 2</Menu.Item>
                        <Menu.Item key="3">nav 3</Menu.Item>
                    </Menu>
                </Header>
                <Content style={{ padding: '0 50px' }}>
                    <Breadcrumb style={{ margin: '16px 0' }}>
                        <Breadcrumb.Item>Home</Breadcrumb.Item>
                        <Breadcrumb.Item>List</Breadcrumb.Item>
                        <Breadcrumb.Item>App</Breadcrumb.Item>
                    </Breadcrumb>
                    <Layout className="site-layout-background" style={{ padding: '24px 0' }}>
                        <Sider className="site-layout-background" width={200}>
                            <Menu
                                mode="inline"
                                defaultSelectedKeys={['1']}
                                defaultOpenKeys={['sub1']}
                                style={{ height: '100%' }}
                            >
                                <Menu.Item key="1">QA Home</Menu.Item>
                                <Menu.Item key="2">Stack</Menu.Item>
                                <Menu.Item key="3">Tags</Menu.Item>
                                <Menu.Item key="4">Users</Menu.Item>
                            </Menu>
                        </Sider>
                        <Content style={{ padding: '0 24px', minHeight: 280 }}>{this.props.children}</Content>
                    </Layout>
                </Content>
                <Footer style={{ textAlign: 'center' }}>Ant Design 	© {getYear()} Created by Ant UED</Footer>
            </Layout>
        )
    }
}


export default BaseLayout;